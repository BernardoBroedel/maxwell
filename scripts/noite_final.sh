#!/usr/bin/env bash
# Teste final: a mesma bateria rodada duas vezes ao mesmo tempo, COM e SEM as notas do cap. 11
# (data/processed/notas_lt), já com o Sadiku caps. 9 a 12 e o material do professor no RAG.
#
# Rode dentro de ~/maxwell-site, num tmux, com:   sudo bash scripts/noite_final.sh
# (um sudo só para a noite inteira). Espera a transcrição do livro terminar antes de começar.
set -uo pipefail
cd "$(dirname "$0")/.."
hora() { date +%H:%M; }

echo "[$(hora)] Esperando a transcrição do livro terminar..."
ultimo=$(date +%s)
while true; do
  if pgrep -f transcrever_livro.py >/dev/null; then
    ultimo=$(date +%s)
  elif [ -f data/processed/sadiku/cap12.md ] || [ $(( $(date +%s) - ultimo )) -gt 900 ]; then
    break
  fi
  sleep 30
done
echo "[$(hora)] Transcrição encerrada:"
ls -la data/processed/sadiku/

echo "[$(hora)] Atualizando o backend do site (código novo + capítulos novos)..."
docker compose up -d --build backend
sleep 20
docker compose logs backend | grep RAG | tail -1

mkdir -p avaliacao/resultados
RODAR="docker compose run --rm -T -v ./scripts:/app/scripts -v ./avaliacao:/app/avaliacao backend uv run --no-sync python"
$RODAR scripts/gerar_bateria.py --escala 0.6

echo "[$(hora)] Rodando as duas baterias (acompanhe com: tail -f avaliacao/resultados/final-*.log)"
$RODAR scripts/avaliar.py --rotulo final-com-notas --arquivo avaliacao/bateria.json --paralelo 2 --juiz \
  > avaliacao/resultados/final-com-notas.log 2>&1 &
$RODAR scripts/avaliar.py --rotulo final-sem-notas --arquivo avaliacao/bateria.json --paralelo 2 --juiz --sem notas_lt \
  > avaliacao/resultados/final-sem-notas.log 2>&1 &
wait

echo "[$(hora)] Pronto. Relatórios:"
ls -la avaliacao/resultados/final-*
