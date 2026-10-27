"use strict";
const allowed = new Set(["round", "cabinet", "tower", "dex"]);
const selected = new URLSearchParams(window.location.search).get("profile");
const profile = allowed.has(selected) ? selected : "round";
const labels = { round: "ROUND MIRROR", cabinet: "MIRROR CABINET", tower: "TRANSPARENT PC", dex: "GALAXY DEX" };
document.getElementById("app").dataset.profile = profile;
document.getElementById("displayLabel").textContent = labels[profile];
document.title = `Smart Surfaces · ${labels[profile]}`;
document.querySelectorAll(".profile-nav a").forEach(link => {
  if (link.dataset.target === profile) link.setAttribute("aria-current", "page");
});
const format = (date, opts) => new Intl.DateTimeFormat("de-DE", opts).format(date);
function clock() {
  const now = new Date();
  const value = format(now, { hour: "2-digit", minute: "2-digit" });
  const el = document.getElementById("clock");
  el.textContent = value;
  el.dateTime = now.toISOString();
  document.getElementById("date").textContent = format(now, { weekday: "long", day: "numeric", month: "long", year: "numeric" });
}
clock();
setInterval(clock, 15000);
async function loadDemo() {
  const status = document.getElementById("status");
  try {
    const response = await fetch("/api/status", { cache: "no-store" });
    if (!response.ok) throw new Error("not available");
    const data = await response.json();
    if (data.schemaVersion !== 1 || data.kind !== "demo") throw new Error("unexpected response");
    const values = [data.roomTempC, data.humidityPercent, data.cpuTempC, data.cpuLoadPercent];
    if (!values.every(Number.isFinite)) throw new Error("invalid data");
    document.getElementById("temperature").textContent = `${data.roomTempC.toFixed(1)} °C`;
    document.getElementById("humidity").textContent = `${data.humidityPercent.toFixed(0)} %`;
    document.getElementById("cpuTemp").textContent = `${data.cpuTempC.toFixed(1)} °C`;
    document.getElementById("cpuLoad").textContent = `${data.cpuLoadPercent.toFixed(0)} %`;
    status.textContent = "Simulierte Messwerte · kein Sensor verbunden";
  } catch {
    status.textContent = "Testdaten nicht verfügbar · lokaler Server prüfen";
  }
}
loadDemo();
setInterval(loadDemo, 30000);
