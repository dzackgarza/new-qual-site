---
title: The sheaf condition
order: 1
topics:
- Sheaves
- Presheaves
- Sheafification
---

# The sheaf condition

The substantive distinction is which sheaf axiom a proposed presheaf violates and what sheafification changes.

[[D-RCCFY]]

[[FE-AM5Z8]]

Two failures, and they are not the same failure: the constant presheaf has sections it cannot glue, and the presheaf of bounded functions has a notion that is not local at all.
The two failures are detected by different axioms.

[[D-0QSI0]]

[[D-COMMACAT]]

[[T-3VX80]]

[[D-A7LCT]]

Sheafification changes no stalk.
Consequently a sequence of sheaves is exact exactly when the corresponding sequence of stalks is exact.
Kernels are computed sectionwise, while the sectionwise presheaf image and cokernel need not be sheaves and are sheafified to obtain the image and cokernel in the sheaf category; their stalks are still the image and cokernel of the stalk maps.

## Sheafification as a space over $X$

The compatible-families formula gives the sheafification explicitly.
The espace étalé gives a geometric realization: a sheaf is a space over $X$ whose projection is a local homeomorphism, and the sections of $\mcf^+$ are its continuous sections.

[[D-VJFAP]]

Two standard facts are immediate from the construction.
Stalks are unchanged because the space was built out of stalks alone, and $\mcf \to \mcf^+$ is an isomorphism exactly when $\mcf$ already had every section the space carries.

[[PR-IP6ZG]]

Colimits are the one place the sheafification refuses to disappear on a general space.
Quasicompactness is what removes it, so the Noetherian hypothesis is substantive rather than decorative.
