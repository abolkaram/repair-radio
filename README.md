# RR-01 / REPAIR RADIO

`CALL SIGN: BENCH OPEN | CARRIER: GENLAYER STUDIONET`

## Symptom signal

A caller freezes a device description, symptoms, known facts, safety exclusions, and ordered diagnostic stages. Distinct community troubleshooters transmit one check each. The contract stores the accepted diagnostic path, stage cursor, fuse budget, and terminal state.

## Bench interlocks

`open_bench` requires substantive facts, two safety exclusions, and at least three stages. `transmit_check` rejects closed benches, duplicate helpers, vague checks, and missing expected observations before AI runs. After consensus, deterministic code advances one stage or trips one fuse, ending at `DIAGNOSED` or `LOCKED_OUT`.

## Diagnostic relay

Validators independently assess every exclusion, current stage, information gain, and whether the expected observation distinguishes plausible causes. Unsafe power, disassembly, bypasses, invented certainty, and non-diagnostic actions are rejected. GenLayer is essential because safety and usefulness require contextual judgment without trusting one remote expert. The interface reads `get_bench`, paged signals, paged benches, and summary views.

## Tuning commands

```text
genvm-lint lint contracts/contract.py
python -m pytest tests/test_surface.py -q
cd frontend
npm install
npm run typecheck
npm run build
```

The static frontend uses `genlayer-js` and no traditional backend. Its oscilloscope, stage tuner, fuse meter, patch console, and interlock lamps explain contract state.

## Sign-off

This is a fictional education workflow, not electrical, appliance, battery, vehicle, medical-device, or professional repair advice.

- Contract: `0x65bf35982dC1434818D0a2dd11E8B5e8C7eEa0e0`
- Deployment: `0x6f120957efeeef7f0b946950f46d0209d7efb6413713cd950720a5fc9331be4e`
- Repository: https://github.com/abolkaram/repair-radio
- Public bench: https://abolkaram-repair-radio.pages.dev/
