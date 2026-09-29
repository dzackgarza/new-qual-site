---
schema: qual/card@1
id: P-AGH253TILDEADJ
kind: problem
title: The tilde and global sections functors are adjoint
classification:
  areas:
  - algebraic-geometry
  topics:
  - Quasi-coherent Sheaves
  - Adjoint Functors
  - Affine Schemes
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the statement and construction with the retained MinerU transcription Hartshorne_Solutions_extracted.md, section 2.5, solution 5.3, and the mapping property in Stacks Project Tag 01I7. Checked the localization and restriction arguments independently.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X = \Spec A$ be an affine scheme.
Show that the functors $\sim$ and $\Gamma$ are adjoint in the following sense: for any $A$-module $M$, and for any sheaf of $\OO_X$-modules $\mcf$, there is a natural isomorphism
$$
\Hom_A(M,\Gamma(X,\mcf))\cong\Hom_{\OO_X}(\widetilde M,\mcf).
$$
:::

::: {.solution}
Use the canonical identifications $\widetilde M(D(f))\cong M_f$ and $\Gamma(X,\widetilde M)\cong M$ [@Har10a, Proposition II.5.1].
For $f\in A$, write $r_f:\mcf(X)\to\mcf(D(f))$ for restriction.

::: pf

::: {.pf-step #s1}

Every $A$-linear map $u:M\to\Gamma(X,\mcf)$ determines an $\OO_X$-linear morphism $\Phi(u):\widetilde M\to\mcf$.

::: pf-proof

The module $\mcf(D(f))$ is an $A_f$-module, so multiplication by $f$ is invertible on it.
The universal property of localization therefore extends $r_f\circ u$ uniquely to an $A_f$-linear map
$$
u_f:M_f\longrightarrow\mcf(D(f)),
\qquad
u_f(m/f^n)=f^{-n}r_f(u(m)).
$$
In particular, the formula is independent of the chosen fraction.

For an inclusion $D(g)\subseteq D(f)$, the restriction of $f$ is a unit on $D(g)$.
Both composites from $M_f$ to $\mcf(D(g))$ obtained using $u_f$, $u_g$, and restriction send $m/1$ to $u(m)|_{D(g)}$ and respect multiplication by $f^{-1}$.
The uniqueness in localization makes these composites equal.
Thus the maps $u_f$ commute with all restrictions between distinguished opens.
Distinguished opens form a basis, so the sheaf gluing axiom extends them uniquely to a morphism $\Phi(u):\widetilde M\to\mcf$.
Its linearity follows on this basis, hence on every open set.

:::

:::

::: {.pf-step #s2}

Taking global sections defines a map $\Psi:\Hom_{\OO_X}(\widetilde M,\mcf)\to\Hom_A(M,\Gamma(X,\mcf))$ inverse to $\Phi$.

::: pf-proof

For $v:\widetilde M\to\mcf$, let $\Psi(v)=v_X$ under $\Gamma(X,\widetilde M)\cong M$.
Taking $f=1$ in step [](#s1){.pf-ref} gives $\Psi(\Phi(u))=u$.

Conversely, compatibility of $v$ with restriction and its $A_f$-linearity give
$$
v_{D(f)}(m/f^n)=f^{-n}r_f(v_X(m)).
$$
This is precisely the formula for $\Phi(\Psi(v))$ on $D(f)$.
The morphisms agree on a basis, so $\Phi(\Psi(v))=v$.
Both constructions preserve addition and multiplication by elements of $A$, giving an isomorphism of $A$-modules.

:::

:::

::: {.pf-step #s3}

The isomorphism is natural in $M$ and $\mcf$.

::: pf-proof

Let $a:M'\to M$ be $A$-linear and let $b:\mcf\to\mcg$ be an $\OO_X$-linear morphism.
The formula of step [](#s1){.pf-ref} gives
$$
\Phi(u\circ a)=\Phi(u)\circ\widetilde a,
\qquad
\Phi(\Gamma(X,b)\circ u)=b\circ\Phi(u).
$$
Indeed, on each $D(f)$ both sides of the first equality send $m'/f^n$ to $f^{-n}u(a(m'))|_{D(f)}$.
Both sides of the second send $m/f^n$ to $f^{-n}b_{D(f)}(u(m)|_{D(f)})$.
These are the naturality identities in the two variables.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} construct the inverse isomorphisms, and step [](#s3){.pf-ref} proves naturality.
Thus $M\mapsto\widetilde M$ is [[D-DEFADJ|left adjoint]] to $\mcf\mapsto\Gamma(X,\mcf)$.

:::

:::

:::
