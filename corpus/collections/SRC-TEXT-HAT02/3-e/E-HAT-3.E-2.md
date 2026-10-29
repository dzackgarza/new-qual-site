---
schema: qual/card@1
id: E-HAT-3.E-2
kind: problem
title: "Homotopy classification of lens spaces"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.E, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
In this problem we will derive one half of the classification of lens spaces up to homotopy equivalence, by showing that if $L_m(\ell_1, \dots, \ell_n) \simeq L_m(\ell_1', \dots, \ell_n')$ then $\ell_1 \cdots \ell_n \equiv \pm \ell_1' \cdots \ell_n' k^n \pmod{m}$ for some integer $k$. The converse is Exercise 29 for §4.2.

(a) Let $L = L_m(\ell_1, \dots, \ell_n)$ and let $\ZZ_m^*$ be the multiplicative group of invertible elements of $\ZZ_m$. Define $t \in \ZZ_m^*$ by the equation $xy^{n-1} = tz$ where $x$ is a generator of $H^1(L; \ZZ_m)$, $y = \beta(x)$, and $z \in H^{2n-1}(L; \ZZ_m)$ is the image of a generator of $H^{2n-1}(L; \ZZ)$. Show that the image $\tau(L)$ of $t$ in the quotient group $\ZZ_m^* / \pm(\ZZ_m^*)^n$ depends only on the homotopy type of $L$.

(b) Given nonzero integers $k_1, \dots, k_n$, define a map $\tilde{f}: S^{2n-1} \to S^{2n-1}$ sending the unit vector $(r_1 e^{i\theta_1}, \dots, r_n e^{i\theta_n})$ in $\CC^n$ to $(r_1 e^{ik_1\theta_1}, \dots, r_n e^{ik_n\theta_n})$. Show:
  (i) $\tilde{f}$ has degree $k_1 \cdots k_n$.
  (ii) $\tilde{f}$ induces a quotient map $f: L \to L'$ for $L' = L_m(\ell_1', \dots, \ell_n')$ provided that $k_j \ell_j \equiv \ell_j' \pmod{m}$ for each $j$.
  (iii) $f$ induces an isomorphism on $\pi_1$, hence on $H^1(-; \ZZ_m)$.
  (iv) $f$ has degree $k_1 \cdots k_n$, i.e., $f_*$ is multiplication by $k_1 \cdots k_n$ on $H_{2n-1}(-; \ZZ)$.

(c) Using the $f$ in (b), show that $\tau(L) = k_1 \cdots k_n \tau(L')$.

(d) Deduce that if $L_m(\ell_1, \dots, \ell_n) \simeq L_m(\ell_1', \dots, \ell_n')$, then $\ell_1 \cdots \ell_n \equiv \pm \ell_1' \cdots \ell_n' k^n \pmod{m}$ for some integer $k$.
:::

::: {.solution}
Write
\[
L=L_m(\ell_1,\dots,\ell_n).
\]
Let $x\in H^1(L;\ZZ_m)$ be a generator, put $y=\beta(x)$, and let $z\in H^{2n-1}(L;\ZZ_m)$ be the reduction of an integral orientation generator. Define $t\in\ZZ_m^*$ by
\[
xy^{n-1}=tz.
\]

::: pf

::: pf-step

The class
\[
\tau(L)=[t]\in\ZZ_m^*/\bigl(\pm(\ZZ_m^*)^n\bigr)
\]
depends only on the homotopy type of $L$.

::: pf-proof

Let $h:L\to L'$ be a homotopy equivalence. For suitable units $a\in\ZZ_m^*$ and a sign $\varepsilon=\pm1$,
\[
h^*(x')=a x,
\qquad
h^*(y')=a y
\]
by naturality of the Bockstein, and
\[
h^*(z')=\varepsilon z
\]
because $h$ has degree $\pm1$ on integral top cohomology. Pulling back
\[
x'(y')^{n-1}=t'z'
\]
gives
\[
a^nxy^{n-1}=\varepsilon t'z,
\]
so
\[
a^nt=\varepsilon t'.
\]
Thus $t$ and $t'$ differ by a sign and an $n$th power of a unit, exactly the ambiguity quotiented out in $\tau$.

:::

:::

::: pf-step

For nonzero integers $k_1,\dots,k_n$, the map
\[
\widetilde f(r_1e^{i\theta_1},\dots,r_ne^{i\theta_n})
=(r_1e^{ik_1\theta_1},\dots,r_ne^{ik_n\theta_n})
\]
has the stated properties.

::: pf-proof

For a regular value with every coordinate nonzero, the $j$th angular coordinate has $|k_j|$ inverse choices, and each local sign contributes $\operatorname{sgn}(k_j)$. Hence the sum of local degrees is
\[
\deg\widetilde f=k_1\cdots k_n.
\]

Let the generator of the $\ZZ_m$ action defining $L$ multiply the $j$th coordinate by
\[
e^{2\pi i\ell_j/m}.
\]
Then $\widetilde f$ carries this action to multiplication in the $j$th target coordinate by
\[
e^{2\pi i k_j\ell_j/m}.
\]
Thus if
\[
k_j\ell_j\equiv\ell_j'\pmod m
\]
for all $j$, $\widetilde f$ is equivariant for the identity automorphism of $\ZZ_m$ and descends to
\[
f:L\to L'.
\]
The induced map on $\pi_1\cong\ZZ_m$ is therefore the identity, hence an isomorphism, and so is the induced map on $H^1(-;\ZZ_m)$.

Finally the covering projections have degree $m$ and fit into the commutative square with $\widetilde f$ and $f$. Multiplicativity of degree gives
\[
m\deg f=(\deg\widetilde f)m,
\]
so
\[
\deg f=k_1\cdots k_n.
\]

:::

:::

::: pf-step

For the map in part 2,
\[
\tau(L)=k_1\cdots k_n\,\tau(L').
\]

::: pf-proof

Since $f_*$ is the identity on $\pi_1$, choose generators with
\[
f^*(x')=x,
\qquad f^*(y')=y.
\]
On top cohomology,
\[
f^*(z')=(k_1\cdots k_n)z.
\]
Pulling back $x'(y')^{n-1}=t'z'$ therefore gives
\[
xy^{n-1}=t'(k_1\cdots k_n)z,
\]
so
\[
t=(k_1\cdots k_n)t'.
\]

:::

:::

::: pf-step

The stated necessary condition for homotopy equivalence follows.

::: pf-proof

Let
\[
L_0=L_m(1,\dots,1).
\]
Choose $k_j$ with
\[
k_j\ell_j\equiv1\pmod m.
\]
Part 3 gives
\[
\tau(L)=\left(\prod_j\ell_j\right)^{-1}\tau(L_0).
\]
Similarly,
\[
\tau(L')=\left(\prod_j\ell_j'\right)^{-1}\tau(L_0).
\]
If $L\simeq L'$, part 1 says these two classes differ by a sign and an $n$th power of a unit. Cancelling the unit $\tau(L_0)$ and inverting the resulting congruence yields
\[
\boxed{\ell_1\cdots\ell_n
\equiv\pm\ell_1'\cdots\ell_n' k^n\pmod m}
\]
for some unit $k$ modulo $m$, represented by an integer $k$.

:::

:::

:::

:::
