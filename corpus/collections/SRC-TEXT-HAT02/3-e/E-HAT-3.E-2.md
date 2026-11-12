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
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    All four parts read and checked. (a) is right: for a homotopy equivalence $h$ one has
    $h^*x'=ax$, $h^*y'=ay$ by naturality of the Bockstein, $h^*z'=\varepsilon z$ with
    $\varepsilon=\pm1$ since $h$ has degree $\pm1$ on integral top cohomology, so $a^nt=\varepsilon t'$
    and the two classes agree in $\ZZ_m^*/(\pm(\ZZ_m^*)^n)$. Added: the same computation shows
    $\tau(L)$ is independent of the chosen generator $x$, which the card used without saying — an
    (b) is right in all four items. The local-degree bookkeeping is about the *angular* extension
    $(r,\theta)\mapsto(r,k_j\theta)$ and is now stated in those terms: in the oriented frame
    $(\partial_r,r^{-1}\partial_\theta)$ the derivative is $\operatorname{diag}(1,k_j)$, so the local degree is
    $\operatorname{sgn}(k_j)$ at each of the $|k_j|$ preimages. An earlier version of *this note* described that
    argument through the holomorphic power $z\mapsto z^{k_j}$; that was wrong, since $z\mapsto z^k$ is conformal on
    $\CC^\times$ with local degree $+1$ for every $k\ne0$, and it is a different map when $k<0$. What is **not**
    certified, and is a named input from the section: that $\widetilde f$ has this derivative and this local degree
    at all, and the degree formula $\deg\widetilde f=\prod_j k_j$ itself, which is the standard computation for
    self-maps of $S^{2n-1}$. <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/LensDegree.lean> certifies only the arithmetic:
    $\det\operatorname{diag}(1,k)=k$, the orientation criterion read off it, and $|k|\operatorname{sgn}(k)=k$ with the
    product over the coordinates, and nothing about the geometric map. The degree of $f$ comes from the covering
    square $p'\circ\widetilde f=f\circ p$ with both coverings of degree $m$, giving $\deg f=\deg\widetilde f$; the
    earlier version of the solution wrote $\deg\widetilde f=m\deg f$, false for $m>1$, and the earlier version of
    this note repeated it.
    rather than an equation with $m$ on both sides. (c) and (d) are right, including the use of
    $L_m(1,\dots,1)$ and of $k_j\equiv\ell_j^{-1}$ to get $\tau(L)=(\prod\ell_j)^{-1}\tau(L_0)$; the
    cancellation is legitimate because $\tau$ takes values in a group. Nothing is left uncited
    except the standard facts on lens spaces quoted from the section.
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
$$
L=L_m(\ell_1,\dots,\ell_n).
$$
Let $x\in H^1(L;\ZZ_m)$ be a generator, put $y=\beta(x)$, and let $z\in H^{2n-1}(L;\ZZ_m)$ be the reduction of an integral orientation generator. Define $t\in\ZZ_m^*$ by
$$
xy^{n-1}=tz.
$$
Replacing $x$ by $ax$ with $a\in\ZZ_m^*$ multiplies $y$ by $a$ and $xy^{n-1}$ by $a^n$, hence multiplies $t$ by $a^n$ and leaves the class of $t$ in $\ZZ_m^*/\bigl(\pm(\ZZ_m^*)^n\bigr)$ unchanged. So $\tau(L)$ does not depend on the choice of generator, which is why the quotient by $n$th powers is the right one; the argument below repeats this computation for a homotopy equivalence.

::: pf

::: pf-step

The class
$$
\tau(L)=[t]\in\ZZ_m^*/\bigl(\pm(\ZZ_m^*)^n\bigr)
$$
depends only on the homotopy type of $L$.

::: pf-proof

Let $h:L\to L'$ be a homotopy equivalence. For suitable units $a\in\ZZ_m^*$ and a sign $\varepsilon=\pm1$,
$$
h^*(x')=a x,
\qquad
h^*(y')=a y
$$
by naturality of the Bockstein, and
$$
h^*(z')=\varepsilon z
$$
because $h$ has degree $\pm1$ on integral top cohomology. Pulling back
$$
x'(y')^{n-1}=t'z'
$$
gives
$$
a^nxy^{n-1}=\varepsilon t'z,
$$
so
$$
a^nt=\varepsilon t'.
$$
Thus $t$ and $t'$ differ by a sign and an $n$th power of a unit, exactly the ambiguity quotiented out in $\tau$.

:::

:::

::: pf-step

For nonzero integers $k_1,\dots,k_n$, the map
$$
\widetilde f(r_1e^{i\theta_1},\dots,r_ne^{i\theta_n})
=(r_1e^{ik_1\theta_1},\dots,r_ne^{ik_n\theta_n})
$$
has the stated properties.

::: pf-proof

For a regular value with every coordinate nonzero, the $j$th angular coordinate has $\abs{k_j}$ inverse choices, and each local sign contributes $\operatorname{sgn}(k_j)$. Hence the sum of local degrees is
$$
\deg\widetilde f=k_1\cdots k_n.
$$
The bookkeeping deserves one clause, and it is about the *angular* extension $(r,\theta)\mapsto(r,k_j\theta)$, not about the holomorphic power $z\mapsto z^{k_j}$: in the oriented frame $(\partial_r,r^{-1}\partial_\theta)$ of the punctured plane the derivative is $\operatorname{diag}(1,k_j)$, with determinant $k_j$, so the $j$th coordinate map has local degree $\operatorname{sgn}(k_j)$ at each of its preimages, and there are $|k_j|$ of them, giving $|k_j|\operatorname{sgn}(k_j)=k_j$. The holomorphic power is a *different* map when $k_j<0$ — it also changes the radius, and its local degree is $+1$ everywhere, because $z\mapsto z^{k_j}$ is conformal on $\CC^\times$ — so it cannot be used here; only the product of the $n$ signs and the $n$ preimage counts gives $k_1\cdots k_n$. The determinant computation behind the sign, $\det\operatorname{diag}(1,k)=k$ together with $|k|\operatorname{sgn}(k)=k$, is certified in <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/LensDegree.lean>.

Let the generator of the $\ZZ_m$ action defining $L$ multiply the $j$th coordinate by
$$
e^{2\pi i\ell_j/m}.
$$
Then $\widetilde f$ carries this action to multiplication in the $j$th target coordinate by
$$
e^{2\pi i k_j\ell_j/m}.
$$
Thus if
$$
k_j\ell_j\equiv\ell_j'\pmod m
$$
for all $j$, $\widetilde f$ is equivariant for the identity automorphism of $\ZZ_m$ and descends to
$$
f:L\to L'.
$$
The induced map on $\pi_1\cong\ZZ_m$ is therefore the identity, hence an isomorphism, and so is the induced map on $H^1(-;\ZZ_m)$.

Finally, the covering projections $p:S^{2n-1}\to L$ and $p':S^{2n-1}\to L'$ both have degree $m$, and they fit into the commutative square $p'\circ\widetilde f=f\circ p$. Multiplicativity of degree applied to the two composites of that square gives, on the one hand
$$
\deg(p'\circ\widetilde f)=\deg(p')\deg(\widetilde f)=m\deg\widetilde f
$$
and on the other
$$
\deg(f\circ p)=\deg(f)\deg(p)=m\deg f,
$$
and the two composites are the same map, so $m\deg\widetilde f=m\deg f$. Since $m\ne0$,
$$
\deg f=\deg\widetilde f=k_1\cdots k_n.
$$
Note that $\widetilde f\ne f\circ p$: that composite has codomain $L'$, not $S^{2n-1}$, and the square is the only relation between the three maps.

:::

:::

::: pf-step

For the map in part 2,
$$
\tau(L)=k_1\cdots k_n\,\tau(L').
$$

::: pf-proof

Since $f_*$ is the identity on $\pi_1$, choose generators with
$$
f^*(x')=x,
\qquad f^*(y')=y.
$$
On top cohomology,
$$
f^*(z')=(k_1\cdots k_n)z.
$$
Pulling back $x'(y')^{n-1}=t'z'$ therefore gives
$$
xy^{n-1}=t'(k_1\cdots k_n)z,
$$
so
$$
t=(k_1\cdots k_n)t'.
$$

:::

:::

::: pf-step

The stated necessary condition for homotopy equivalence follows.

::: pf-proof

Let
$$
L_0=L_m(1,\dots,1).
$$
Choose $k_j$ with
$$
k_j\ell_j\equiv1\pmod m.
$$
Part 3 gives
$$
\tau(L)=\left(\prod_j\ell_j\right)^{-1}\tau(L_0).
$$
Similarly,
$$
\tau(L')=\left(\prod_j\ell_j'\right)^{-1}\tau(L_0).
$$
If $L\simeq L'$, part 1 says these two classes differ by a sign and an $n$th power of a unit. Cancelling the unit $\tau(L_0)$ and inverting the resulting congruence yields
$$
\boxed{\ell_1\cdots\ell_n
\equiv\pm\ell_1'\cdots\ell_n' k^n\pmod m}
$$
for some unit $k$ modulo $m$, represented by an integer $k$.

:::

:::

:::

:::
