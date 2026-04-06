interface HealthResponse {
  status: string;
}

async function checkHealth(): Promise<void> {
  const statusEl = document.querySelector<HTMLParagraphElement>('#status');
  if (!statusEl) return;

  try {
    const res = await fetch('/api/health');
    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const data: HealthResponse = await res.json();
    statusEl.textContent = `バックエンド: ${data.status}`;
  } catch {
    statusEl.textContent = 'バックエンドに接続できませんでした';
  }
}

checkHealth();
