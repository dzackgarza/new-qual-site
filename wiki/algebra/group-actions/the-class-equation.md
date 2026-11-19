---
title: The class equation
order: 20
topics:
- Conjugacy
- Centralizers and Normalizers
- Center of Groups
---

# The class equation

Under conjugation, a finite group falls into classes whose sizes are indices of centralizers, so every class size divides $\size{G}$ and the classes of size one are the central elements.
The count is what forces a $p$-group to have a nontrivial center, and the $p$-group statements here rest on that.

[[C-O7CP3]]

## $p$-groups

[[E-6AOD7]]

[[T-4CDTT]]

For a group of order $p^k$ the count gives the following: it is abelian when $k=2$, it is nilpotent for every $k$, its maximal subgroups are normal of index $p$, and it is simple exactly when $k=1$.

[[PR-IGLFV]]

[[P-7H5CP]]

[[E-AMD-Y5JUYURM]]

[[P-NZOMZ]]

## Burnside's lemma

[[C-HE5SL]]

[[FD-XRRNZ]]

::: {.remark title="Counting orbits"}
Burnside's lemma counts orbits, such as colorings of the beads of a necklace or of the faces of a cube up to the action of a rotation group.
For $g,h\in G$, the map $x\mapsto hx$ is a bijection $\Fix(g)\to\Fix(hg\inverseof{h})$, so $\size{\Fix(g)}$ depends only on the conjugacy class of $g$, and the sum may be taken over conjugacy classes, each weighted by its size.
:::
