# Individual Incentives

Evaluate multi-agent cooperation under private objectives and shared survival risk.

Four agents share a damaged space station, limited batteries, and six rounds until rescue. Each sees private cargo values and sensor readings, negotiates through public and private messages, and commits actions simultaneously. Each agent earns rewards for its own cargo objectives, while station failure penalizes everyone.

## Harder V2 environment

[V2 mechanics and usage](docs/v2.md) add hidden faults, scenario-specific repair recipes, coupled life-support resources, delayed repairs, costly investigation, specialist roles, escrowed trades, and private contracts. Four difficulty tiers span 6–36 rounds. It supports independent model players, varied partner policies, held-out evaluation, and supplied training checkpoints.

```sh
python3 -m individual_incentives_eval v2 run --plan examples/v2-baselines.json \
  --out ../eval-runs/v2 --difficulty hard --seeds 100 --rotations 4
```

The existing commands below retain V1. The earlier GPT pilot is not a V2 model ranking.

## Run

Python 3.11+ is sufficient. Local baselines require no dependencies or API credentials.

```sh
python3 -m individual_incentives_eval run \
  --plan examples/baselines.json \
  --out ../eval-runs/individual-incentives-eval \
  --seeds 10 --rotations 4 --probes

python3 -m individual_incentives_eval replay \
  ../eval-runs/individual-incentives-eval/episodes/individual--one-selfish--s0--r0--n0.json \
  --out ../eval-runs/individual-incentives-eval/replay.html

python3 -m unittest discover -s tests -v
```

The default eval is `individual`. The alternative reward scheme remains available through `--eval both` for controlled comparisons. This repository has its own Python package (`individual_incentives_eval`) and runs independently.

## Included

- A seeded simulation with isolated observations and simultaneous actions.
- Baseline policies, command adapters, and a JSON chat-completions adapter.
- Rotated seat assignments, matched scenarios, isolated prediction probes, and resumable batches.
- Survival and objective metrics, resource accounting, and scenario-bootstrap intervals.
- Offline HTML replays and physically redacted seat exports.

External model adapters require explicit opt-in and can incur charges. Keep runtime logs outside Git. The included results cover scripted baselines and an exploratory GPT subscription pilot: 15 of 16 model games completed. No RL training has been performed. See the [pilot results and chart](docs/pilot-results.md) for outcomes and limitations.

[Protocol](docs/protocol.md) · [Model adapters, evaluation plans, and RL API](docs/usage.md) · [Verification](docs/verification.md)
