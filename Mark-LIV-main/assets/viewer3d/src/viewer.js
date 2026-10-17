import * as THREE from "three";

const state = { markers: [], target: null, spin: true, ready: false };
const canvas = document.getElementById("c");
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
renderer.setClearColor(0x000308, 1);
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 100);
camera.position.set(0, 0, 4.2);

const globe = new THREE.Group();
scene.add(globe);
const cyan = 0x00d4ff;

const sphere = new THREE.Mesh(
  new THREE.SphereGeometry(1, 48, 32),
  new THREE.MeshBasicMaterial({ color: cyan, wireframe: true, transparent: true, opacity: 0.18 })
);
globe.add(sphere);
globe.add(new THREE.Mesh(
  new THREE.SphereGeometry(0.985, 32, 24),
  new THREE.MeshBasicMaterial({ color: 0x001018, transparent: true, opacity: 0.85 })
));

const rings = [];
for (let i = 0; i < 3; i++) {
  const ring = new THREE.Mesh(
    new THREE.RingGeometry(1.25 + i * 0.12, 1.26 + i * 0.12, 128),
    new THREE.MeshBasicMaterial({ color: cyan, transparent: true, opacity: 0.35 - i * 0.08, side: THREE.DoubleSide })
  );
  ring.rotation.x = Math.PI / 2.3 + i * 0.25;
  scene.add(ring);
  rings.push(ring);
}

function toVec(lat, lon, r) {
  const phi = (90 - lat) * Math.PI / 180;
  const theta = (lon + 180) * Math.PI / 180;
  return new THREE.Vector3(
    -r * Math.sin(phi) * Math.cos(theta),
    r * Math.cos(phi),
    r * Math.sin(phi) * Math.sin(theta)
  );
}

function resize() {
  const w = canvas.clientWidth || 1, h = canvas.clientHeight || 1;
  renderer.setSize(w, h, false);
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
}
window.addEventListener("resize", resize);

// Rotation that brings (lat, lon) to face the camera (+z).
function rotationFor(lat, lon) {
  const target = toVec(lat, lon, 1).normalize();
  return new THREE.Quaternion().setFromUnitVectors(target, new THREE.Vector3(0, 0, 1));
}

let last = performance.now();
function frame(now) {
  const dt = Math.min(0.1, (now - last) / 1000);
  last = now;
  if (state.target) {
    globe.quaternion.slerp(state.target, Math.min(1, dt * 3));
    if (globe.quaternion.angleTo(state.target) < 0.005) {
      globe.quaternion.copy(state.target);
    }
  } else if (state.spin) {
    globe.rotation.y += dt * 0.25;
  }
  rings.forEach((r, i) => { r.rotation.z += dt * (0.2 + i * 0.1); });
  renderer.render(scene, camera);
  requestAnimationFrame(frame);
}

function num(v, lo, hi, name) {
  const n = Number(v);
  if (!Number.isFinite(n) || n < lo || n > hi) throw new Error(name + " out of range");
  return n;
}

window.jarvisViewer = {
  flyTo(lat, lon) {
    state.target = rotationFor(num(lat, -90, 90, "lat"), num(lon, -180, 180, "lon"));
    state.spin = false;
  },
  addMarker(lat, lon, label) {
    lat = num(lat, -90, 90, "lat"); lon = num(lon, -180, 180, "lon");
    const dot = new THREE.Mesh(
      new THREE.SphereGeometry(0.025, 12, 12),
      new THREE.MeshBasicMaterial({ color: 0xffd400 })
    );
    dot.position.copy(toVec(lat, lon, 1.01));
    globe.add(dot);
    state.markers.push({ lat, lon, label: String(label || "").slice(0, 60), obj: dot });
  },
  clearMarkers() {
    state.markers.forEach(m => globe.remove(m.obj));
    state.markers = [];
  },
  spin(on) { state.spin = !!on; if (on) state.target = null; },
  getState() {
    return {
      ready: state.ready,
      spin: state.spin,
      flying: !!state.target,
      markers: state.markers.map(m => ({ lat: m.lat, lon: m.lon, label: m.label })),
    };
  },
};

resize();
state.ready = true;
requestAnimationFrame(frame);
