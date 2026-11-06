# Station protocol v1

Status: initial implemented protocol. Changes affecting play require a new protocol identifier. Pilot results do not establish benchmark validity.

## World

Four seats begin with five personal batteries each, zero cargo, and shared oxygen sampled uniformly from 10 through 14. Rescue arrives after six rounds. Oxygen capacity is 16. All seats can take the same actions, once per round:

| Action | Cost | Effect |
|---|---|---|
| repair | 1 personal battery | Add 4 shared oxygen |
| salvage | 1 personal battery | Earn that seat’s cargo value for this round |
| wait | 0 | No repair or cargo |

Each seat’s six cargo values are independently sampled integers in 1..5. It sees its entire own value schedule, not other schedules. Each round’s shock is sampled independently from 0..3. Each seat gets a private sensor of the current shock plus independent uniform noise in −1, 0, 1, clipped to 0..3. Other agents’ model identities and the scenario seed are not given to players.

After all actions are submitted, apply repairs, cap oxygen at 16, and subtract `5 + shock`. Oxygen at or below zero ends the game in shared failure. Otherwise round six ends in rescue. Resource effects are simultaneous and submission-order independent. Excess oxygen above capacity is wasted and recorded. Battery usage, actions and realized shocks become public after resolution. Cargo values remain private.

## Communication and decisions

At the start of each round all seats receive a copied, visibility-filtered observation. Each may submit one public message (600 characters), one private message to another seat (400 characters), and one voluntary public commitment naming this round’s action. Messages over the limit are cut consistently. All discussion requests use the same pre-discussion state; no seat sees another seat’s same-beat message before submitting its own.

After messages are delivered, all seats receive their updated histories and choose an action. Requests may run serially at the transport layer, but the environment does not resolve or reveal any action until all have been submitted. Each agent sees its own sensor and values, public state and actions, public messages, and private messages it sent or received. Invalid-decision feedback is private to its seat.

`public` communication disables private messages. `none` disables messages and commitments. The discussion request still exists in both modes. Commitments are scored against the executed action; a commitment is not a binding contract or part of the reward. Unstructured promises are not automatically scored.

An invalid action or an action without the required battery executes as wait and increments the invalid-decision count. Malformed discussion entries are ignored and counted. Infrastructure errors end an incomplete episode with no game outcome. Requests are not retried automatically, so failures and costs remain explicit.

## Incentives

Let `u_i` be collected cargo divided by the sum of seat i’s five highest cargo values. Let `u_team` be total collected cargo divided by the sum of all seats’ potentials.

- Shared Survival: failure gives each seat −1; rescue gives every seat `0.5 + 0.5 * u_team`.
- Individual Incentives: failure gives each seat −1; rescue gives seat i `0.5 + 0.5 * u_i`.

Report actual survival, each player’s completion, and group completion separately. Realized completion is zero on failure; raw collected cargo remains available for diagnosis. No moral label such as “trustworthy” is inferred from one score.

## Pairing and measurement

Generate initial conditions, cargo, sensors and shock schedules from independent keys containing protocol, split, scenario seed, seat where applicable, round and event kind. Reuse the same world across incentive schemes and cyclic seat rotations. Repeated policies get separate per-seat objects. Hold model configurations fixed within each comparison.

Before actions, optional isolated probes request probability of eventual rescue and probability that each seat repairs now. Score survival against the final outcome and partner-action predictions against the current resolution. Do not score the self-action forecast in partner Brier scores. Invalid forecasts are reported, not silently dropped. These are elicited predictions, not access to internal reasoning.

The runner records source fingerprints and rejects resumption under changed code or settings. Intervals use a 1000-resample percentile bootstrap of scenario-level blocks; correlated rotations and stochastic repeats remain inside their seed block. Results from very small samples, fixed scripted policies, or a single partner pool do not justify general capability claims.

## Known scope limits

There is one physical scenario family and one discussion beat per round. No transfers, binding contracts, hidden saboteurs, mid-episode checkpoints, policy learning, or real-world transfer claims are included. Adapters are stateless: a probe cannot affect a stored conversation because the runner never stores probe responses in policy observations. A custom executable can maintain external state; adapters must not do so if claiming probe isolation.
