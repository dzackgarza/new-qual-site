---
schema: qual/card@1
id: E-UU8CC
kind: problem
title: The degree of a map of the circle
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: Aleksey Zinger, MAT 530: Topology & Geometry I,
    Fall 2005, Problem Set 9, "Solution to Problem p366, #9", PDF pp. 3-6 of the sheet
    (tmp/sources/munkres-solutions-zinger-mat530-ps9.pdf), and against Munkres, Topology (2000),
    Section 58 Exercise 9, printed p. 366. Zinger defines $\deg h$ by $h_*=(\deg h)\hat\alpha$ and
    proves the five parts: independence of the path and the base point, invariance under homotopy,
    multiplicativity, the degrees of the constant map, the identity, the reflection and $z\mapsto z^n$,
    and that equal degree implies homotopic. The card proves the same five using the naturality of the
    change-of-basepoint isomorphism and the preferred generators, and its (c) is the same computation
    as Zinger's. Nothing needed repair.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the five parts of Munkres, Topology (2000), Section 58 Exercise 9, printed p. 366, following Zinger MAT 530 Problem Set 9 "Solution to Problem p366, #9" PDF pp. 3-6. Each assertion the prose made in one clause is now a step with its justification: path-independence of the preferred generator (quoted from the exercise, because abelianness is what makes it true), the naturality identity for change of basepoint (proved on one loop, where the identity h of the reverse path equals the reverse of h alpha is what makes it work), and in part (e) the periodicity of a lift, which the prose passed over in silence: t -> H(t+1) - H(t) is continuous into the discrete group Z, hence constant, and its value is the degree by Theorem 54.5. Part (e) also now names the quotient map R x I -> S^1 x I that carries the straight-line homotopy of the lifts down to S^1. Theorem 54.5 printed p. 345 and the homotopy lemma in the proof of Theorem 54.3 printed p. 342 are cited where used. Nothing in the statement needed repair; the exercise's own claim that the degree is independent of the choice of gamma is used, not reproved.
---

::: {.exercise}

We define the degree of a continuous map $h: S^1 \to S^1$ as follows.

Let $b_0$ be the point $(1, 0)$ of $S^1$; choose a generator $\gamma$ for the infinite cyclic group $\pi_1(S^1, b_0)$.
If $x_0$ is any point of $S^1$, choose a path $\alpha$ in $S^1$ from $b_0$ to $x_0$, and define $\gamma(x_0) = \hat{\alpha}(\gamma)$.
Then $\gamma(x_0)$ generates $\pi_1(S^1, x_0)$.
The element $\gamma(x_0)$ is independent of the choice of the path $\alpha$, since the fundamental group of $S^1$ is abelian.

Now given $h: S^1 \to S^1$, choose $x_0 \in S^1$ and let $h(x_0) = x_1$.
Consider the homomorphism

$$
h_*: \pi_1(S^1, x_0) \to \pi_1(S^1, x_1).
$$

Since both groups are infinite cyclic, we have

$$
h_*(\gamma(x_0)) = d \cdot \gamma(x_1)
$$

for some integer $d$, if the group is written additively.
The integer $d$ is called the degree of $h$ and is denoted by $\deg h$.

The degree of $h$ is independent of the choice of the generator $\gamma$; choosing the other generator would merely change the sign of both sides.

(a) Show that $d$ is independent of the choice of $x_0$.

(b) Show that if $h, k: S^1 \to S^1$ are homotopic, they have the same degree.

(c) Show that $\deg(h \circ k) = (\deg h) \cdot (\deg k)$.

(d) Compute the degrees of the constant map, the identity map, the reflection map $\rho(x_1, x_2) = (x_1, -x_2)$, and the map $h(z) = z^n$, where $z$ is a complex number.

(e) Show that if $h, k: S^1 \to S^1$ have the same degree, they are homotopic.
:::

::: {.solution}
The five parts are proved as Zinger does in **Aleksey Zinger, MAT 530, Fall 2005, Problem Set 9, "Solution to Problem p366, #9", PDF pp. 3--6**, which defines $\deg h$ by $h_*(\gamma)=(\deg h)\gamma$ and proves the same properties; the exercise is Munkres, *Topology* (2000), Section 58 Exercise 9, printed p. 366.

Throughout, $\gamma(x)$ denotes the preferred generator of $\pi_1(S^1,x)$ built from $\gamma=\gamma(b_0)$ in the exercise, and $\hat\alpha$ denotes the change-of-basepoint isomorphism along a path $\alpha$, so that $\hat\alpha:\pi_1(S^1,x)\to\pi_1(S^1,y)$ for $\alpha$ from $x$ to $y$.

::: pf

::: {.pf-step #preferred}
If $\alpha$ is a path in $S^1$ from $x$ to $y$, then $\hat\alpha\big(\gamma(x)\big)=\gamma(y)$.

::: pf-proof
Let $\alpha_0$ be a path from $b_0$ to $x$ and $\alpha_1$ a path from $b_0$ to $y$. By definition $\gamma(x)=\widehat{\alpha_0}(\gamma)$ and $\gamma(y)=\widehat{\alpha_1}(\gamma)$. The path $\alpha_0*\alpha$ also runs from $b_0$ to $y$, so $\gamma(y)=\widehat{\alpha_0*\alpha}(\gamma)=\hat\alpha\big(\widehat{\alpha_0}(\gamma)\big)=\hat\alpha(\gamma(x))$, using that change of basepoint along a concatenation is the composite of the two changes. The exercise states that $\gamma(y)$ does not depend on the path chosen, since $\pi_1(S^1,b_0)$ is abelian, so no choice made here matters.
:::

:::

::: {.pf-step #naturality}
Let $h:S^1\to S^1$, let $\alpha$ be a path from $x_0$ to $x'_0$, and put $\beta=h\circ\alpha$. Then
$$
\widehat\beta\circ h_{*,x_0}=h_{*,x'_0}\circ\hat\alpha .
$$

::: pf-proof
Both sides are homomorphisms $\pi_1(S^1,x_0)\to\pi_1(S^1,h(x'_0))$, so it suffices to compare them on one loop $f$ at $x_0$. On the left, $\widehat\beta\big(h_*([f])\big)=[\,\overline{\beta}*(h\circ f)*\beta\,]$, and on the right $h_{*,x'_0}\big(\hat\alpha([f])\big)=h_*\big([\,\overline{\alpha}*f*\alpha\,]\big)=[\,(h\circ\overline\alpha)*(h\circ f)*(h\circ\alpha)\,]$. The paths $\overline\beta=h\circ\overline\alpha$ and $\beta=h\circ\alpha$ are equal, since $h$ applied to the reverse of $\alpha$ reverses $h\circ\alpha$. So the two loops agree, and homotopy classes of loops at a point are compared in $\pi_1(S^1,h(x'_0))$.
:::

:::

::: {.pf-step #indepbase}
Part (a): the integer $d$ with $h_*\big(\gamma(x_0)\big)=d\,\gamma\big(h(x_0)\big)$ does not depend on $x_0$.

::: pf-proof
Let $x_0,x'_0\in S^1$ with integers $d,d'$, choose a path $\alpha$ from $x_0$ to $x'_0$, and put $x_1=h(x_0)$, $x'_1=h(x'_0)$, $\beta=h\circ\alpha$. Then
$$
h_{*,x'_0}\big(\gamma(x'_0)\big)
=h_{*,x'_0}\big(\hat\alpha(\gamma(x_0))\big)
=\widehat\beta\big(h_{*,x_0}(\gamma(x_0))\big)
=\widehat\beta\big(d\,\gamma(x_1)\big)
=d\,\gamma(x'_1),
$$
where the second equality is step [](#naturality){.pf-ref} and the third and fourth use that $\hat\alpha$ and $\widehat\beta$ send preferred generators to preferred generators (step [](#preferred){.pf-ref}) and are homomorphisms. Since $\gamma(x'_1)$ is a generator of the infinite cyclic group $\pi_1(S^1,x'_1)$, the integer $d'$ in $h_{*,x'_0}(\gamma(x'_0))=d'\,\gamma(x'_1)$ is unique, so $d'=d$.
:::

:::

::: {.pf-step #homotopy}
Part (b): if $h\simeq k$, then $\deg h=\deg k$.

::: pf-proof
Let $H:S^1\times I\to S^1$ be a homotopy from $h$ to $k$, fix $x_0$, and let $\eta(t)=H(x_0,t)$, a path from $h(x_0)$ to $k(x_0)$. The homotopy lemma in the proof of Theorem 54.3 (Munkres, printed p. 342) states that for every loop $f$ at $x_0$ the loops $\eta*(h\circ f)*\overline\eta$ and $k\circ f$ are homotopic rel $\{0,1\}$, that is,
$$
k_{*,x_0}=\widehat\eta\circ h_{*,x_0}.
$$
Applying both sides to $\gamma(x_0)$ and using $h_{*,x_0}(\gamma(x_0))=(\deg h)\gamma(h(x_0))$,
$$
k_{*,x_0}\big(\gamma(x_0)\big)=(\deg h)\,\widehat\eta\big(\gamma(h(x_0))\big)=(\deg h)\,\gamma(k(x_0))
$$
by step [](#preferred){.pf-ref}. The integer multiplying the generator $\gamma(k(x_0))$ in $k_{*,x_0}(\gamma(x_0))$ is by definition $\deg k$, and it is unique, so $\deg h=\deg k$.
:::

:::

::: {.pf-step #multiplicative}
Part (c): $\deg(h\circ k)=(\deg h)(\deg k)$.

::: pf-proof
Let $x_0\in S^1$, $x_1=k(x_0)$ and $x_2=h(x_1)$. Then $k_{*,x_0}(\gamma(x_0))=(\deg k)\gamma(x_1)$, and applying the homomorphism $h_{*,x_1}$,
$$
(h\circ k)_{*,x_0}\big(\gamma(x_0)\big)=h_{*,x_1}\big(k_{*,x_0}(\gamma(x_0))\big)=(\deg k)\,h_{*,x_1}\big(\gamma(x_1)\big)=(\deg k)(\deg h)\,\gamma(x_2).
$$
The composite $h\circ k$ is continuous, and the integer multiplying $\gamma\big((h\circ k)(x_0)\big)=\gamma(x_2)$ is $\deg(h\circ k)$ by definition, so $\deg(h\circ k)=(\deg h)(\deg k)$.
:::

:::

::: {.pf-step #examples}
Part (d): the constant map has degree $0$, the identity has degree $1$, the reflection $\rho(x_1,x_2)=(x_1,-x_2)$ has degree $-1$, and $h(z)=z^n$ has degree $n$.

::: pf-proof
In each case $x_0=b_0$ is fixed by the map except in the last, so $\gamma(x_1)=\gamma(b_0)=\gamma$ and the degree is the integer $d$ with $h_*(\gamma)=d\gamma$.

::: {.pf-step #constant}
A constant map induces the trivial homomorphism, so $d=0$.
:::

::: {.pf-step #identity}
The identity induces the identity isomorphism, so $d=1$.
:::

::: {.pf-step #reflection}
On the circle $\rho$ is $z\mapsto\bar z$, and with $\omega(t)=e^{2\pi it}$ one has $\rho\circ\omega=\overline\omega$. Since $\omega$ represents $\gamma$, $\rho_*(\gamma)=[\overline\omega]=-\gamma$, so $d=-1$.
:::

::: {.pf-step #power}
With $h(z)=z^n$ one has $h\circ\omega=\omega_n$, where $\omega_n(t)=e^{2\pi int}$, and $\omega_n$ is the $n$-fold concatenation of $\omega$ with itself, so $[\omega_n]=n[\omega]$ and $d=n$; in the loop model $[\omega]$ corresponds to $1\in\ZZ$ under the isomorphism of Theorem 54.5 (printed p. 345), which sends a class to the endpoint of its lift starting at $0$, and $\omega_n$ lifts to $t\mapsto nt$.
:::

:::

:::

::: {.pf-step #converse}
Part (e): if $\deg h=\deg k$, then $h\simeq k$.

::: pf-proof
Write $q:\RR\to S^1$ for $q(t)=e^{2\pi it}$, a covering map. By the lifting criterion the maps $h\circ q$ and $k\circ q$, whose domain $\RR$ is simply connected, lift to $\tilde h,\tilde k:\RR\to\RR$ with $q\circ\tilde h=h\circ q$ and $q\circ\tilde k=k\circ q$; shifting a lift by an integer keeps it a lift, so take $\tilde h(0)=\tilde k(0)=0$.

::: {.pf-step #period}
$\tilde h(t+1)=\tilde h(t)+\deg h$ and $\tilde k(t+1)=\tilde k(t)+\deg k$ for all $t$.

::: pf-proof
Because $q(t+1)=q(t)$, we get $q\big(\tilde h(t+1)\big)=h\big(q(t+1)\big)=h\big(q(t)\big)=q\big(\tilde h(t)\big)$, so $\tilde h(t+1)-\tilde h(t)\in q^{-1}(1)=\ZZ$. The function $t\mapsto\tilde h(t+1)-\tilde h(t)$ is continuous and $\ZZ$ is discrete, so it is constant, and its value is $\tilde h(1)-\tilde h(0)$. The loop $h\circ\omega=q\circ\tilde h$ restricted to $\abs{0,1}$ is a loop at $b_0$ lifts to the path $\tilde h$ from $\tilde h(0)=0$ to $\tilde h(1)$, so under the isomorphism of Theorem 54.5 the class $h_*(\gamma)$ corresponds to $\tilde h(1)-\tilde h(0)$; since $h_*(\gamma)=(\deg h)\gamma$ corresponds to $\deg h$, that value is $\deg h$. The same argument gives $\tilde k(t+1)-\tilde k(t)=\deg k$.
:::

:::

::: {.pf-step #straightline}
If $\deg h=\deg k=d$, then $h\simeq k$.

::: pf-proof
For $s\in I$ define $\widetilde L_s(t)=(1-s)\tilde h(t)+s\tilde k(t)$. By step [](#period){.pf-ref}, $\widetilde L_s(t+1)=\widetilde L_s(t)+d$ for all $s,t$.
Set $\widetilde F(t,s)=q\big(\widetilde L_s(t)\big)=e^{2\pi i\widetilde L_s(t)}$, continuous on $\RR\times I$. It is invariant under $t\mapsto t+1$: $\widetilde F(t+1,s)=e^{2\pi i(\widetilde L_s(t)+d)}=\widetilde F(t,s)$. The map $\pi:\RR\times I\to S^1\times I$, $\pi(t,s)=(q(t),s)$, is a quotient map, being the product of the quotient map $q$ and the identity of the compact space $I$ (Theorem 22.2, printed p. 141), so $\widetilde F$ factors through it: there is a continuous $F:S^1\times I\to S^1$ with $F\big(q(t),s\big)=q(\widetilde L_s(t))$. At $s=0$, $F(q(t),0)=q(\tilde h(t))=h(q(t))$; at $s=1$, $F(q(t),1)=k(q(t))$. Since $q$ is onto, $F(-,0)=h$ and $F(-,1)=k$, so $F$ is a homotopy from $h$ to $k$.
:::

:::

:::

:::

:::
:::
