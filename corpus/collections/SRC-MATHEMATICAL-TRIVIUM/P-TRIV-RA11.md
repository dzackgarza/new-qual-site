---
schema: qual/card@1
id: P-TRIV-RA11
kind: problem
title: 'Huygens problem: amplifying velocity through a chain of elastic collisions'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 11, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: problem
"Huygens problem".
Consider the ball with mass M moving with velocity V towards another ball with mass m that stays at rest.
After the central collision, the second ball acquires the velocity

$$
v = { \frac { 2 M } { m + M } } V .\tag{11}
$$

This expression can be obtained using the momentum and energy conservation laws for the two-body system.
One can observe that $V \leqslant v \leqslant 2 V$ as far as $0 \leqslant m \leqslant M$ One may ask under what conditions the limit $v \leqslant 2 V$ can be broken to make v arbitrary large.
A possible solution is to insert a chain of balls staying at rest with intermediate masses $m _ { 1 } , . . . , m _ { n }$ such that $m < m _ { 1 } < . . . < m _ { n } < M$ between the two original bodies, and to transfer the kinetic energy of the moving ball to the ball with mass m through a sequence of intermediate central collisions.

(a) Applying Eq.(11) to the sequence of central collisions between the balls, deduce how one should choose the masses $m _ { 1 } , . . . , m _ { n }$ to yield the maximal velocity of the ball with mass m.

(b) Assuming $m \ll M$ , investigate the limit $n \to \infty$
:::
