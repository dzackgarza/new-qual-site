---
schema: qual/card@1
id: P-UWALG07-5
kind: problem
title: A UFD is integrally closed; integral closures of $k[x,y]/(x^2-y^3)$ and $k[x,y,z]/(x^2-y^2z)$
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Integral Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement read from the card in `corpus/collections/SRC-UW-ALG-2007`; no correction is claimed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    (a) the classical fraction argument: if $f=a/b$ in lowest terms is integral then $b\mid a^n$,
    hence $b$ is a unit. (b) the integral closure of $k[x,y]/(x^2-y^3)$ is $k[t]$ with $x=t^3$,
    $y=t^2$, obtained as $k[y,x/y]$. (c) the integral closure of $k[x,y,z]/(x^2-y^2z)$ is
    $k[y,x/y]\cong k[Y,U]$, using the hint's element $u=x/y$ with $u^2=z$. In both cases the candidate
    is a polynomial ring, hence a UFD and integrally closed, is integral over the ring, and has the
    same fraction field. Nothing is left in outline.
---
---

::: {.problem}
Let $A$ be a domain and $K$ its field of fractions.
Recall that we say $f\in K$ is *integral over* $A$ if it satisfies an equation
$$
f^n+a_{n-1}f^{n-1}+\cdots+a_1f+a_0=0,
$$
where $a_{n-1},\ldots,a_0\in A$.
The *integral closure* $\tilde A\subset K$ of $A$ is the set of $f\in K$ which are integral over $A$, and we say $A$ is *integrally closed* if $\tilde A=A$.

(a) Show that a UFD is integrally closed.
(Hint: write $f$ as a fraction.)

(b) Compute the integral closure of $k[x,y]/(x^2-y^3)$.
(Remember that a polynomial ring is a UFD and therefore integrally closed.)

(c) Compute the integral closure of $k[x,y,z]/(x^2-y^2z)$.
(Hint: there is an obvious integral element.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Part (a): a UFD is integrally closed.

::: pf-proof

Let $A$ be a UFD with fraction field $K$, and let $f\in K$ be integral over $A$. Write $f=a/b$ with $a,b\in A$ having no common irreducible factor; we may take $b\ne0$. If
$$
f^n+c_{n-1}f^{n-1}+\cdots+c_1f+c_0=0,\qquad c_i\in A,
$$
multiply by $b^n$:
$$
a^n+c_{n-1}a^{n-1}b+\cdots+c_1ab^{n-1}+c_0b^n=0,
$$
so $a^n=-b\bigl(c_{n-1}a^{n-1}+\cdots+c_0b^{n-1}\bigr)$, that is $b\mid a^n$ in $A$. If $b$ were not a unit, some irreducible $\pi$ would divide $b$, hence $\pi\mid a^n$, hence $\pi\mid a$ since $\pi$ is prime in a UFD — contradicting coprimality. So $b$ is a unit and $f=a/b\in A$. Hence $\tilde A=A$.

:::

:::

::: {.pf-step #s2}

Part (b): the integral closure of $A=k[x,y]/(x^2-y^3)$ is $k[t]$, with $x\mapsto t^3$ and $y\mapsto t^2$.

::: pf-proof

Let $u,v$ denote the classes of $x,y$ in $A$, so that $A=k[u,v]$ with $u^2=v^3$, and let $K=k(u,v)$ be its fraction field.

*The candidate.* Put $t=u/v\in K$. Then
$$
t^2=\frac{u^2}{v^2}=\frac{v^3}{v^2}=v,\qquad t^3=t\cdot t^2=\frac{u}{v}\cdot v=u .
$$
So $K$ contains $t$ with $v=t^2$ and $u=t^3$, and $B=k[t]\subseteq K$ contains $A=k[u,v]=k[t^3,t^2]$. Moreover $K=k(u,v)=k(t)$, so $B$ and $A$ have the same fraction field.

*$B$ is integral over $A$.* $t$ satisfies $T^2-v=0$ with $v\in A$, so $t$ is integral over $A$; hence every element of $B=k[t]$ is integral over $A$.

*$B$ is integrally closed.* $B=k[t]$ is a polynomial ring over a field, hence a UFD, hence integrally closed by part [](#s1){.pf-ref}.

*Conclusion.* $A\subseteq B\subseteq K$, $B$ integral over $A$ and integrally closed; so $B$ contains the integral closure $\tilde A$ of $A$ (as $\tilde A$ is the smallest integrally closed ring between $A$ and $K$) and is contained in it (as every element of $B$ is integral over $A$). Hence $\tilde A=B=k[t]$.

:::

:::

::: {.pf-step #s3}

Part (c): the integral closure of $A=k[x,y,z]/(x^2-y^2z)$ is $k[y,u]$ with $u=x/y$, i.e. a polynomial ring in two variables.

::: pf-proof

Write $A=k[X,Y,Z]/(X^2-Y^2Z)$ and let $x,y,z$ be the images, so $x^2=y^2z$ and $A=k[x,y,z]$.

*The obvious integral element.* Put $u=x/y\in K=\operatorname{Frac}(A)$. Then
$$
u^2=\frac{x^2}{y^2}=\frac{y^2z}{y^2}=z\in A,
$$
so $u$ is integral over $A$, being a root of $T^2-z$.

*The candidate.* Let $B=k[y,u]\subseteq K$. Since $z=u^2$ and $x=uy$, we have $A=k[x,y,z]\subseteq k[y,u]=B$. Since $B$ contains $y$ and $u=x/y$, $K=\operatorname{Frac}(A)\subseteq\operatorname{Frac}(B)$; and $B\subseteq K$ gives the reverse inclusion. So $B$ and $A$ have the same fraction field.

*$B$ is integral over $A$.* Both generators are: $y\in A$, and $u$ satisfies $T^2-z=0$ with $z\in A$. Hence $B$ is integral over $A$.

*$B$ is integrally closed.* $B=k[y,u]$ is a polynomial ring in two variables over a field, hence a UFD, hence integrally closed by part [](#s1){.pf-ref}. Concretely $B\cong k[Y,U]$ via $Y\mapsto y$, $U\mapsto u$, which is an isomorphism because $y,u$ are algebraically independent: they are the two coordinates in the presentation $A=k[y,u]$ obtained by eliminating $x=uy$ and $z=u^2$ from the relation $x^2=y^2z$.

*Conclusion.* As in part [](#s2){.pf-ref}, $A\subseteq B\subseteq K$ with $B$ integral over $A$ and integrally closed, so $\tilde A=B=k[y,x/y]$.

:::

:::

::: {.pf-step #s4}

Both answers are normalizations of plane and threefold curves, and the generators found are the ones the geometry predicts.

::: pf-proof

In (b), $A=k[t^2,t^3]$ is the coordinate ring of the cuspidal cubic, whose normalization is the affine line $k[t]$; the conductor is $(t^2,t^3)$-primary and $B/A$ is not finite free but is finite (generated by $1,t$). In (c), $A=k[y,uy,u^2]$ with the single relation, and $B=k[y,u]$ is the coordinate ring of a smooth surface, so the singular locus of $\operatorname{Spec}A$ is where $y=0$; again the normalization is $B$.

:::

:::

:::

:::
