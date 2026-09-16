---
title: The sheaf condition
order: 1
topics:
- Sheaves
- Presheaves
- Sheafification
---

# The sheaf condition

The definition is short and is never the question.
What is asked is which axiom a proposed presheaf violates, and what sheafification does about it.

[[D-RCCFY]]

[[FE-AM5Z8]]

Two failures, and they are not the same failure: the constant presheaf has sections it cannot glue, and the presheaf of bounded functions has a notion that is not local at all.
Naming which axiom breaks is the whole of the answer.

[[D-0QSI0]]

[[D-COMMACAT]]

[[T-3VX80]]

[[D-A7LCT]]

Sheafification changes no stalk.
That single sentence settles most follow-ups, because it forces every construction whose definition is stalk-local — kernels, images, exactness — to be insensitive to whether one sheafified.
The constructions that are not stalk-local, cokernels first among them, are exactly the ones that need it.

## Sheafification as a space over $X$

The compatible-families formula is correct and tells nobody why it is the right formula.
The espace étalé does: a sheaf is a space over $X$ whose projection is a local homeomorphism, and the sections of $\mcf^+$ are its continuous sections.

[[D-VJFAP]]

Read the two standard facts off the construction rather than proving them again.
Stalks are unchanged because the space was built out of stalks alone, and $\mcf \to \mcf^+$ is an isomorphism exactly when $\mcf$ already had every section the space carries.

[[PR-IP6ZG]]

Colimits are the one place the sheafification refuses to disappear on a general space.
Quasicompactness is what removes it, so the Noetherian hypothesis is doing real work and should be quoted, not omitted.
