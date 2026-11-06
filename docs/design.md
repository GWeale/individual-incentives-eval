# Design and acceptance

Two versioned evaluations share one station simulation. `shared` uses a common crew reward; `individual` uses each seat’s private cargo utility. Both penalize shared failure. Model, scenario seed, seat rotation, action budgets, communication mode and protocol version are recorded.

## Data and ownership

`Scenario` owns immutable initial conditions and a pre-generated six-round hazard schedule. `StationEnv` owns the discuss/act/terminal state machine, legal actions, visibility-filtered events and mechanical scoring. `Agent.respond(observation, phase)` receives only a copied seat observation. The runner owns model calls, isolated probes, run manifests, atomic persistence and paired summaries. The replay is an exported, offline HTML file; no server or hosted service is required.

An alternative would implement two unrelated games. A shared engine better isolates incentives as the experimental variable and avoids drifting rules. A general simulation framework would add interfaces before there is a second physical world to model.

## Execution checkpoint

- Blocking first steps: freeze the observation/action contracts and reward definitions before runners or UI.
- Independent workstreams: engine, runner and replay share a changing contract; keep one writer for this initial implementation.
- Shared mutable state: each episode owns its environment, agents and output file. No shared conversation or random generator across seats.
- Smallest safe decomposition: one lead builds engine, then runner and adapters, then viewer, with behavior checks at each boundary.

## Acceptance

Both evals must run from the public CLI without credentials, produce valid six-round successes and early failures, preserve private information, settle joint actions without submission-order effects, and use identical hazards across matched runs. A held-out split must occupy a distinct scenario seed namespace. Batch resumption must reject configuration changes and keep errors visible. A command-based model adapter must be exercised end to end. Replays must show actual observations, messages and actions, support round and viewpoint selection, and keep omniscient output separate from seat exports.

Local baseline evaluation is a mechanics check. It is not an LLM leaderboard or evidence of training effectiveness. No training or paid inference runs are part of this implementation.
