---
schema: qual/card@1
id: E-HAT-3.2-3
kind: problem
title: Maps $\RP^n\to\RP^m$ for $n>m$ and the Borsuk--Ulam theorem
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 3; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both parts: over $\ZZ_2$, $f^*(\alpha_m)=\alpha_n$ forces
    $0=f^*(\alpha_m^{m+1})=\alpha_n^{m+1}\ne0$ when $m+1\le n$, and for $\CP^n\to\CP^m$ the same
    computation gives $d^{m+1}\beta_n^{m+1}=0$ in a torsion-free group, so $d=0$; the Borsuk-Ulam
    half handles $n=0$ and $n=1$ separately and otherwise uses the equivariant $g$, whose induced
    map on $\RP^n\to\RP^{n-1}$ is nontrivial on $H^1(\ZZ_2)$.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 3 (p.229) with both parts, including the printed display defining g and the inequality f(x) != f(-x). Rechecked (a): over Z_2 the ring is Z_2[alpha]/(alpha^{m+1}) by Theorem 3.19 p.220, so f^* alpha_m = alpha_n forces 0 = f^*(alpha_m^{m+1}) = alpha_n^{m+1} != 0 when m+1 <= n; over Z the ring is Z[beta]/(beta^{m+1}) by Example 3.12 p.213, so d^{m+1} beta_n^{m+1} = 0 in the torsion-free group H^{2m+2} forces d = 0. Rechecked (b): the antipodal-equivariant g descends to RP^n -> RP^{n-1}, and the loop joining antipodal points upstairs projects to the nontrivial loop, so (a) applies. Citations added for Proposition 3.10 p.210 (f^* a ring map), Theorem 3.19 p.220 and Example 3.12 p.213. Not covered: the n = 0 and n = 1 cases of (b) are argued separately, as the card states.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, which was already complete. Made the
    small cases of Borsuk-Ulam (n = 0 and n = 1) their own step, and separated the construction of
    the equivariant g from the verification that the descended map is nonzero on H^1, which the prose
    argued in a clause: a path in S^n from x to -x maps to a path between antipodal points of S^{n-1},
    so its projection is the nontrivial class in pi_1(RP^{n-1}) = Z_2, and H^1(-;Z_2) is Hom(pi_1, Z_2)
    on a space with pi_1 = Z_2. Checked the cup-product contradictions in both (a) parts, including
    that beta_n^{m+1} spans a torsion-free group because m+1 <= n. The page numbers were then
    checked: the retained PDF at tmp/sources/hatcher-2002-algebraic-topology.pdf was searched page by
    page and each cited statement located, with printed page = PDF page - 9; Theorem 3.19 is printed
    on p. 220 (PDF 229), Proposition 3.10 on p. 210 (PDF 219) and Example 3.12 on p. 213 (PDF 222),
    all as the card cites them.
---

::: {.problem}
(a) Using the cup product structure, show there is no map $\RP^n \to \RP^m$ inducing a nontrivial map $H^1(\RP^m; \ZZ_2) \to H^1(\RP^n; \ZZ_2)$ if $n > m$.
What is the corresponding result for maps $\CP^n \to \CP^m$?

(b) Prove the Borsuk–Ulam theorem by the following argument.
Suppose on the contrary that $f: S^n \to \RR^n$ satisfies $f(x) \neq f(-x)$ for all $x$.
Then define $g: S^n \to S^{n-1}$ by $g(x) = \bigl(f(x) - f(-x)\bigr) / \norm{f(x) - f(-x)}$, so $g(-x) = -g(x)$ and $g$ induces a map $\RP^n \to \RP^{n-1}$.
Show that part (a) applies to this map.
:::

::: {.solution}
This is Hatcher Exercise 3.2.3, both parts. No published solution set is transcribed: the argument is the card's own, and the numbered results are Hatcher's Theorem 3.19 (p. 220), Proposition 3.10 (p. 210) and Example 3.12 (p. 213).

::: pf

::: {.pf-step #rp}
(a) If $n>m$, no map $f\colon\RP^{n}\to\RP^{m}$ induces a nonzero map $H^{1}(\RP^{m};\ZZ_{2})\to H^{1}(\RP^{n};\ZZ_{2})$.

::: pf-proof
With $\ZZ_{2}$ coefficients, $H^{*}(\RP^{r};\ZZ_{2})\cong\ZZ_{2}[\alpha]/(\alpha^{r+1})$ with $\alpha$ of degree $1$ (Theorem 3.19, p. 220). Write $\alpha_{n},\alpha_{m}$ for the generators. Both $H^{1}$ groups are one-dimensional over $\ZZ_{2}$, so a nonzero $f^{*}$ on $H^{1}$ forces $f^{*}(\alpha_{m})=\alpha_{n}$. Since $f^{*}$ is a ring homomorphism (Proposition 3.10, p. 210), $f^{*}(\alpha_{m}^{m+1})=(f^{*}\alpha_{m})^{m+1}=\alpha_{n}^{m+1}$. But $\alpha_{m}^{m+1}=0$ in $H^{*}(\RP^{m})$, so $\alpha_{n}^{m+1}=0$, contradicting $\alpha_{n}^{m+1}\neq0$ in $H^{m+1}(\RP^{n})$ because $m+1\leq n$. So $f^{*}$ is zero on $H^{1}$.
:::
:::

::: {.pf-step #cp}
(a) For $n>m$, every map $f\colon\CP^{n}\to\CP^{m}$ induces the zero map $H^{2}(\CP^{m};\ZZ)\to H^{2}(\CP^{n};\ZZ)$.

::: pf-proof
$H^{*}(\CP^{r};\ZZ)\cong\ZZ[\beta]/(\beta^{r+1})$ with $\beta$ of degree $2$ (Example 3.12, p. 213). Write $f^{*}(\beta_{m})=d\beta_{n}$ for some integer $d$. Then
$$0=f^{*}(\beta_{m}^{m+1})=d^{m+1}\beta_{n}^{m+1},$$
and $\beta_{n}^{m+1}\neq0$ spans the torsion-free group $H^{2m+2}(\CP^{n};\ZZ)$ because $m+1\leq n$, so $d^{m+1}=0$ and hence $d=0$. So the induced map is zero.
:::
:::

::: {.pf-step #small}
(b) Borsuk--Ulam holds for $n=0$ and $n=1$.

::: pf-proof
For $n=0$ the target $\RR^{0}$ is a single point, so $f(x)=f(-x)$ for the two points of $S^{0}$. For $n=1$, choose a path $\gamma$ in $S^{1}$ from $x$ to $-x$; the continuous function $y\mapsto f(y)-f(-y)$ takes opposite values at $\gamma(0)$ and $\gamma(1)$, so it vanishes somewhere on the path, giving $f(y)=f(-y)$.
:::
:::

::: {.pf-step #equivariant}
(b) If $f\colon S^{n}\to\RR^{n}$ satisfies $f(x)\neq f(-x)$ for all $x$ with $n\geq2$, then $g(x)=\frac{f(x)-f(-x)}{\norm{f(x)-f(-x)}}$ is continuous and antipodal-equivariant, so it descends to a map $\bar g\colon\RP^{n}\to\RP^{n-1}$.

::: pf-proof
The denominator never vanishes by hypothesis, so $g$ is continuous, and $g(-x)=\frac{f(-x)-f(x)}{\norm{f(-x)-f(x)}}=-g(x)$. An equivariant map of spheres descends to the quotients by the antipodal action, which are the real projective spaces, giving $\bar g$ with $\bar g\circ\pi_{n}=\pi_{n-1}\circ g$ for the quotient maps $\pi$.
:::
:::

::: {.pf-step #nontrivial}
$\bar g$ is nonzero on $H^{1}(-;\ZZ_{2})$.

::: pf-proof
It suffices to see that $\bar g$ is nonzero on $\pi_{1}$, since $H^{1}(-;\ZZ_{2})=\Hom(\pi_{1},-;\ZZ_{2})$ and $\pi_{1}(\RP^{k})=\ZZ_{2}$ is generated by the projection of any path joining antipodal points. Choose a path $\gamma$ in $S^{n}$ from $x$ to $-x$; its projection is the generator of $\pi_{1}(\RP^{n})$. The path $g\circ\gamma$ runs from $g(x)$ to $g(-x)=-g(x)$, that is between antipodal points of $S^{n-1}$, so its projection is a loop in $\RP^{n-1}$ joining antipodal points, hence the nontrivial class. So $(\bar g)_{*}$ carries the generator to the generator, and $\bar g^{*}$ is nonzero on $H^{1}$.
:::
:::

::: {.pf-step #conclude}
(b) Some $x\in S^{n}$ satisfies $f(x)=f(-x)$ for every continuous $f\colon S^{n}\to\RR^{n}$.

::: pf-proof
Suppose not, with $n\geq2$. Steps [](#equivariant){.pf-ref} and [](#nontrivial){.pf-ref} produce a map $\bar g\colon\RP^{n}\to\RP^{n-1}$ that is nonzero on $H^{1}$, and $n>n-1$, so part (a) applied with $m=n-1$ says no such map exists. The contradiction proves the theorem, and steps [](#small){.pf-ref} cover $n=0,1$.
:::
:::
:::

:::
