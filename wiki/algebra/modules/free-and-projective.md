---
title: Free and projective modules
order: 20
topics:
- Free Modules
- Projective Modules
---

# Free and projective modules

The properties that separate once the ring is not a PID.

## Free modules, rank, and torsion

A free module is one with a basis, so after choosing that basis it is a direct sum of
copies of the ring.  Rank counts those copies.  Over a domain, freeness forces
torsion-freeness because a nonzero scalar cannot kill a nonzero coordinate vector; the
torsion submodule and annihilator record exactly where that cancellation fails for a
general module.

[[D-LIEMF]]

[[D-IGB7I]]

[[FD-CVEAI]]

[[PR-DLPTR]]

[[D-ZJJ7G]]

[[FF-CY5EA]]

[[FD-BPUNZ]] [[FD-U6KUJ]]

[[FD-SK4ON]]

[[PR-4K4XZ]]

## Projective modules

Projective modules retain the splitting property of free modules without requiring a
basis.  Equivalently, they are direct summands of free modules, which is why every free
module is projective and why projectivity is the right hypothesis for splitting short
exact sequences.  Over a PID, finitely generated torsion-free modules are free, so the
distinctions below collapse; over a general ring they do not.

[[D-RHJMK]]

[[FD-6XJ7D]]

[[PR-RPL4Q]]

:::{.remark title="The hierarchy"}
For finitely generated modules over an integral domain,
\[
\text{free} \implies \text{projective} \implies \text{flat} \implies \text{torsion-free}
,\]
with no arrow reversing in general and all four coinciding over a PID.
Which arrow a problem is asking about is usually decided by the ring, so read the ring first.

:::
