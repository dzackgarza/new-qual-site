---
schema: qual/card@1
id: FD-BIAA7
kind: definition
title: Proof of the Schwarz lemma from the power series of $f$
prompts:
- How is the Schwarz lemma proved from the power series of $f$?
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Maximum Modulus Principle
relations: []
review: draft
---

::: {.proof}
Let $f\colon\DD\to\DD$ be holomorphic with $f(0)=0$, as in the [[T-DAETF|Schwarz lemma]].
Write $f(z)=\sum_{k\ge0}c_kz^k$ on $\DD$.
Since $f(0)=0$, $c_0=0$.
Define $g(z)\coloneqq f(z)/z$ for $z\in\DD\setminus\{0\}$ and $g(0)\coloneqq c_1=f'(0)$.
Then $g(z)=\sum_{k\ge1}c_kz^{k-1}$ on $\DD$, a power series converging on $\DD$, so $g$ is [[D-E7A5W|holomorphic]] on $\DD$.

Fix $0<r<1$.
For $\abs{z}=r$, $\abs{g(z)}=\abs{f(z)}/r<1/r$ because $f$ maps into $\DD$.
By the [[T-BYNL5|maximum modulus principle]] applied to $g$ on the disc $\abs{z}<r$, $\abs{g(z)}\le1/r$ for $\abs{z}\le r$.
For fixed $z\in\DD$, letting $r\to1$ through values $r>\abs{z}$ gives $\abs{g(z)}\le1$.
Hence $\abs{f(z)}\le\abs{z}$ for $z\in\DD$, and $\abs{f'(0)}=\abs{g(0)}\le1$.

If $\abs{f(z_0)}=\abs{z_0}$ for some $z_0\neq0$, then $\abs{g(z_0)}=1$; if $\abs{f'(0)}=1$, then $\abs{g(0)}=1$.
In either case $\abs{g}\le1$ on $\DD$ attains the value $1$ at a point of $\DD$, so $\abs{g}$ has a local maximum there and $g$ is constant on a neighborhood of that point by the maximum modulus principle.
By the [[C-F2ZZQ|identity theorem]], $g\equiv\lambda$ on $\DD$ for a constant $\lambda$ with $\abs{\lambda}=1$, so $f(z)=\lambda z$.
:::
