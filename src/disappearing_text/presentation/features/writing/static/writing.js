/**
 * @file Browser script of the writing page: sends the text on every input,
 * polls the state and shows the countdown, the warning and the text gone message.
 */
(function () {
  "use strict";

  const EMPTY_MESSAGE = document.getElementById("status").textContent;
  const GONE_MESSAGE = "Your text is gone. Start typing again.";

  const editor = document.getElementById("editor");
  const countdown = document.getElementById("countdown");
  const status = document.getElementById("status");
  const pollInterval = Number(document.body.dataset.pollInterval);

  // Counts input events; a poll started before the latest input is stale.
  let inputCount = 0;
  // Posts not yet answered; a poll could overtake them and report old text.
  let pendingPosts = 0;
  let pollRunning = false;

  /** Show one of the four states and its message. */
  function showState(state) {
    let name = "state-empty";
    if (state.was_cleared) {
      name = "state-gone";
    } else if (state.seconds_left !== null) {
      name = state.is_warning ? "state-warning" : "state-typing";
    }
    document.body.className = name;
    document.body.dataset.state = name;

    if (state.seconds_left !== null && !state.was_cleared) {
      const seconds = state.seconds_left.toFixed(1);
      countdown.textContent = state.is_warning
        ? "!! Seconds left: " + seconds + " - keep writing !!"
        : "Seconds left: " + seconds;
      countdown.hidden = false;
    } else {
      countdown.textContent = "";
      countdown.hidden = true;
    }

    if (name === "state-gone") {
      status.textContent = GONE_MESSAGE;
      status.hidden = false;
    } else if (name === "state-empty") {
      status.textContent = EMPTY_MESSAGE;
      status.hidden = false;
    } else {
      status.textContent = "";
      status.hidden = true;
    }
  }

  /** Apply a state answer; only a cleared text empties the text area. */
  function applyState(state) {
    if (state.was_cleared) {
      editor.value = "";
    }
    showState(state);
  }

  async function sendText() {
    inputCount += 1;
    const thisInput = inputCount;
    pendingPosts += 1;
    try {
      const response = await fetch("/api/text", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: editor.value }),
      });
      if (response.ok && thisInput === inputCount) {
        applyState(await response.json());
      }
    } catch (error) {
      console.error("Could not send the text", error);
    } finally {
      pendingPosts -= 1;
    }
  }

  async function poll() {
    if (pollRunning || pendingPosts > 0) {
      return;
    }
    pollRunning = true;
    const startedAt = inputCount;
    try {
      const response = await fetch("/api/state");
      if (response.ok) {
        const state = await response.json();
        if (startedAt === inputCount && pendingPosts === 0) {
          applyState(state);
        }
      }
    } catch (error) {
      console.error("Could not read the state", error);
    } finally {
      pollRunning = false;
    }
  }

  editor.addEventListener("input", sendText);
  window.setInterval(poll, pollInterval);
  editor.focus();
})();
