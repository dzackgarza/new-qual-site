---
schema: qual/card@1
id: E-HAT-4.3-7
kind: problem
title: "Addition in $\\langle X, K(G,n) \\rangle$ matches cohomology"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.

- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof. The prose asserted $\mu^*u=\operatorname{pr}_1^*u+
    \operatorname{pr}_2^*u$ from Exercise 6 and "the Künneth identification"; the card now
    proves it from unitality of the $H$-space structure alone, by restricting the difference to
    the $n$-skeleton of $K\times K$, which is the union of the two factors because $K(G,n)$ is
    $(n-1)$-connected with a single $0$-cell. That removes the appeal to Künneth, which does not
    apply to $K(G,n)$ without finiteness hypotheses. The isomorphism
    $H^n(X;G)\approx\langle X,K(G,n)\rangle$ is cited at printed pp. 393–395. Statement re-read
    in Hatcher, §4.3 Exercise 7, printed p. 419, the page carrying the exercise. Not claimed: a
    retained solution set; the Hatcher sets in `tmp/sources` do not reach this exercise, so the
    argument is the card's own.
---

::: {.problem}
Using an H-space multiplication $\mu$ on $K(G, n)$, define an addition in $\langle X, K(G, n) \rangle$ by $[f] + [g] = [\mu(f, g)]$ and show that under the bijection $H^n(X; G) \approx \langle X, K(G, n) \rangle$ this addition corresponds to the usual addition in cohomology.
:::

::: {.solution}
The statement is Hatcher, *Algebraic Topology* (2002), §4.3 Exercise 7, printed p. 419. No retained solution set covers this exercise — the Hatcher sets in `tmp/sources` do not reach §4.3 Exercise 7 — so the argument below is the card's own; it rests on the isomorphism $H^n(X;G)\approx\langle X,K(G,n)\rangle$ proved in §4.3, printed pp. 393–395, and on the fact that $K(G,n)$ is $(n-1)$-connected with a single $0$-cell.

Throughout $K=K(G,n)$, $K\times K$ carries the product cell structure of two copies of a CW structure on $K$ with one $0$-cell, $\mu:K\times K\to K$ is the $H$-space multiplication and $u\in H^n(K;G)$ corresponds to the identity of $G$ under $H^n(K;G)\approx\operatorname{Hom}(G,G)$.

::: pf

::: {.pf-step #universal}
There is a class $u\in H^n(K;G)$ such that for every CW complex $X$ the map $\Phi:\langle X,K\rangle\to H^n(X;G)$, $\Phi([f])=f^*u$, is a bijection, natural in $X$.

::: pf-proof
By the universal coefficient theorem $H^n(K;G)\approx\operatorname{Hom}(H_n(K),G)=\operatorname{Hom}(G,G)$, and $u$ is the class of the identity. That $\Phi$ is a bijection for every CW complex $X$ is the isomorphism $H^n(X;G)\approx\langle X,K(G,n)\rangle$ of §4.3, printed pp. 393–395; naturality, $\Phi([f\circ h])=h^*\Phi([f])$, is the functoriality of $H^n$ together with $(f\circ h)^*u=h^*f^*u$.

:::

:::

::: {.pf-step #units}
$\mu$ is unital up to homotopy: if $i_1,i_2:K\to K\times K$ are the two factor inclusions, then $\mu\circ i_1\simeq\operatorname{pr}_1$ and $\mu\circ i_2\simeq\operatorname{pr}_2$, so $i_1^*\mu^*u=u=i_2^*\mu^*u$.

::: pf-proof
The defining property of an $H$-space multiplication is that the two composites $K\xrightarrow{i_1}K\times K\xrightarrow{\mu}K$ and $K\xrightarrow{i_2}K\times K\xrightarrow{\mu}K$ are homotopic to the identity, which is what $\operatorname{pr}_1\circ i_1=\mathrm{id}=\operatorname{pr}_2\circ i_2$ says. Applying $H^n(-;G)$ to these homotopies gives $i_1^*\mu^*u=(\mu\circ i_1)^*u=\mathrm{id}^*u=u$, and likewise for $i_2$.

:::

:::

::: {.pf-step #product}
$\mu^*u=\operatorname{pr}_1^*u+\operatorname{pr}_2^*u$ in $H^n(K\times K;G)$.

::: pf-proof
Put $d=\mu^*u-\operatorname{pr}_1^*u-\operatorname{pr}_2^*u$. Both sides lie in $H^n(K\times K;G)$. Since $K$ is $(n-1)$-connected, a CW structure on it with a single $0$-cell has all cells of dimension $\ge n$; a cell of $K\times K$ is a product of a cell of dimension $i$ with one of dimension $j$, so a cell of dimension $\le n$ has $i=0$ or $j=0$, that is, lies in $K\times\{*\}$ or in $\{*\}\times K$. Hence $(K\times K)^{(n)}=(K^{(n)}\times\{*\})\cup(\{*\}\times K^{(n)})$. Restriction to the $n$-skeleton is an isomorphism in degree $n$, since $H^n(X,X^{(n)})=0=H^{n-1}(X,X^{(n)})$ for a CW pair, so it suffices to check $d$ on that union: on the first factor $i_1^*d=u-u-0=0$ by step [](#units){.pf-ref} and because $\operatorname{pr}_2\circ i_1$ is the constant map to the basepoint, whose pullback kills the positive-degree class $u$; on the second factor $i_2^*d=u-0-u=0$ for the same reason. A class on the union of two subcomplexes meeting in a point with vanishing restriction to each is zero, by Mayer–Vietoris. So $d=0$.

:::

:::

::: {.pf-step #homomorphism}
For $[f],[g]\in\langle X,K\rangle$ the addition $[f]+[g]=[\mu(f,g)]$ is well defined, and $\Phi([f]+[g])=\Phi([f])+\Phi([g])$.

::: pf-proof
The class $[\mu(f,g)]$ depends only on $[f]$ and $[g]$, since $\mu$ and the pairing $(f,g)$ are homotopy invariant in each variable. Applying step [](#product){.pf-ref} to the composite $(f,g):X\to K\times K$,
$$
[\mu(f,g)]^*u=(f,g)^*\mu^*u=(f,g)^*\bigl(\operatorname{pr}_1^*u+\operatorname{pr}_2^*u\bigr)=f^*u+g^*u ,
$$
using functoriality $\operatorname{pr}_1\circ(f,g)=f$ and $\operatorname{pr}_2\circ(f,g)=g$. The right-hand side is $\Phi([f])+\Phi([g])$.

:::

:::

::: {.pf-step #conclusion}
Under $\Phi$ the addition $[f]+[g]=[\mu(f,g)]$ on $\langle X,K(G,n)\rangle$ corresponds to the usual addition in $H^n(X;G)$; in particular the $H$-space addition is abelian, with $[\,\mathrm{const}\,]$ as identity and $[f]\mapsto[\mu(f,\iota f)]$ as inverse for a homotopy inverse $\iota$ of the multiplication.

::: pf-proof
Step [](#homomorphism){.pf-ref} says $\Phi$ carries the $H$-space addition to addition of cohomology classes, and step [](#universal){.pf-ref} says $\Phi$ is a bijection. A bijection carrying one composition law to another makes the first a group law exactly when the second is, so $\langle X,K\rangle$ with $[\mu(f,g)]$ is an abelian group isomorphic to $(H^n(X;G),+)$, the constant map corresponding to $0$ and the inverse supplied by the homotopy inverse of $\mu$ that an $H$-space structure provides (§4.3 Exercise 6, printed p. 419).

:::

:::

:::
:::
