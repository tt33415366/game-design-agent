(function attachLatchlineRules(global) {
  "use strict";

  function startRun() {
    return { section: 1, hull: 4, cargo: 0, status: "active", events: [] };
  }

  function copyState(state) {
    return {
      section: state.section,
      hull: state.hull,
      cargo: state.cargo,
      status: state.status,
      events: state.events.map(function copyEvent(event) { return Object.assign({}, event); }),
    };
  }

  function legalActions(section) {
    if (section === 1 || section === 3) return ["Retrieve", "Mark"];
    if (section === 2) return ["Stabilize", "Strip"];
    return [];
  }

  function applyAction(state, action) {
    var next = copyState(state);
    if (next.status !== "active" || legalActions(next.section).indexOf(action) === -1) return next;

    var resolvedSection = next.section;
    if (resolvedSection === 1 && action === "Retrieve") {
      next.cargo += 2;
      next.hull -= 1;
    } else if (resolvedSection === 2 && action === "Stabilize") {
      next.hull = Math.min(4, next.hull + 1);
    } else if (resolvedSection === 2 && action === "Strip") {
      next.cargo += 1;
    } else if (resolvedSection === 3 && action === "Retrieve") {
      next.cargo += 3;
      next.hull -= 3;
    }

    var outcome = "section-resolved";
    if (next.hull <= 0) {
      next.hull = 0;
      next.status = "lost";
      outcome = "hull-breach";
    } else if (resolvedSection < 3) {
      next.section += 1;
    } else if (next.cargo >= 5) {
      next.status = "extracted";
      outcome = "extracted";
    } else {
      next.status = "lost";
      outcome = "cargo-target-missed";
    }

    next.events.push({
      order: next.events.length + 1,
      section: resolvedSection,
      action: action,
      hull: next.hull,
      cargo: next.cargo,
      status: next.status,
      outcome: outcome,
    });
    return next;
  }

  global.LatchlineRules = {
    startRun: startRun,
    applyAction: applyAction,
    legalActions: legalActions,
  };
}(window));
