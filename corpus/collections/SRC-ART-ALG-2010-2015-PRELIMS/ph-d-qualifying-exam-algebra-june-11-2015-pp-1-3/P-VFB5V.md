---
schema: qual/card@1
id: P-VFB5V
kind: problem
title: When $X^{p^n}-X+1$ is irreducible over $\mathbb{F}_p$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared all four Frobenius and irreducibility assertions with June 2015 Fields 3 in the retained extraction; corrected the algebra classification."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the Frobenius-fixed-field construction, the affine root recurrence, irreducibility in both positive cases, and the integer divisibility excluding all other positive n."
---

::: {.problem}
Let $p$ be prime, $n$ be a positive integer, $f(X) = X^{p^n} - X + 1$, and $K$ be an algebraic closure of $\mathbb{F}_p$.

a. If $\alpha \in K$ is a root of $f(X)$ and $a \in \mathbb{F}_{p^n} \subseteq K$, show that $\alpha + a$ is a root of $f(X)$ and $\alpha^p - \alpha + 1 \in \mathbb{F}_{p^n}$.

b. Show that $X^p - X + 1$ is irreducible in $\mathbb{F}_p[X]$.

c. Show that $X^{2^2} - X + 1$ is irreducible in $\mathbb{F}_2[X]$.

d. Show that if $f(X)$ is irreducible in $\mathbb{F}_p[X]$, then $n = 1$ or $n = 2 = p$.
:::

::: solution
We will prove that the two cases in part (d) are exactly the
irreducible cases.

<1>1. For each positive integer $m$, the roots in $K$ of
$X^{p^m}-X$ form a field with $p^m$ elements.

::: proof
The polynomial splits in the algebraically closed field $K$,
and its derivative is $-1$, so its $p^m$ roots are distinct.
In characteristic $p$, the binomial theorem and iteration give
$(u+v)^{p^m}=u^{p^m}+v^{p^m}$. The fixed elements of the map
$u\mapsto u^{p^m}$ are therefore closed under addition and
subtraction, and also under multiplication and nonzero inversion.
They contain $0,1$, so they form a field with exactly $p^m$
elements. We denote this subfield of $K$ by $\mathbb F_{p^m}$.
Its degree over $\mathbb F_p$ is $m$, by counting elements in
a finite-dimensional vector space over $\mathbb F_p$.
:::

<1>2. The two assertions in part (a) hold.

::: proof
Write $q=p^n$. Since $f(\alpha)=0$, we have
$\alpha^q=\alpha-1$. For $a\in\mathbb F_q$, step <1>1 gives
$a^q=a$. Therefore
$$
f(\alpha+a)=\alpha^q+a^q-\alpha-a+1=0.
$$
Put $\beta=\alpha^p-\alpha+1$. Taking $q$th powers gives
$$
\begin{aligned}
\beta^q
&=(\alpha^q)^p-\alpha^q+1\\
&=(\alpha-1)^p-(\alpha-1)+1\\
&=\alpha^p-\alpha+1=\beta.
\end{aligned}
$$
Hence $\beta\in\mathbb F_q$, again by step <1>1.
:::

<1>3. Every root of $f$ lies in $\mathbb F_{p^{np}}$.

::: proof
Starting with $\alpha^{p^n}=\alpha-1$, induction on $j\geq1$
gives
$$
\alpha^{p^{jn}}=\alpha-j,
$$
where the integer $j$ is viewed in the prime field. Indeed,
raising the equality to the $p^n$th power subtracts one more,
because every element of the prime field is fixed by Frobenius.
At $j=p$ we obtain $\alpha^{p^{np}}=\alpha$, proving the claim.
:::

<1>4. The polynomial $X^p-X+1$ is irreducible over $\mathbb F_p$,
proving part (b).

::: proof
Let $\alpha$ be any root. With $n=1$, step <1>3 puts
$\mathbb F_p(\alpha)$ inside $\mathbb F_{p^p}$.
Its degree $d$ over $\mathbb F_p$ divides $p$ by the tower law,
so $d=1$ or $p$. But $a^p-a+1=1$ for every $a\in\mathbb F_p$,
so $\alpha\notin\mathbb F_p$ and $d\ne1$.
Thus $d=p$. The monic minimal polynomial of $\alpha$ divides
$X^p-X+1$ and has the same degree, so it equals that polynomial.
:::

<1>5. The polynomial $X^4+X+1$ is irreducible over $\mathbb F_2$,
proving part (c).

::: proof
It takes value $1$ at both $0$ and $1$, so it has no linear factor.
The only monic irreducible quadratic over $\mathbb F_2$ is
$q(X)=X^2+X+1$: a monic quadratic $X^2+aX+b$ without a root
at zero must have $b=1$, and absence of a root at one then
forces $a=1$.

Modulo $q$, the residue class $x$ satisfies $x^2=x+1$ and
$x^4=(x+1)^2=x^2+1=x$. Consequently $x^4+x+1=1$, so
$q$ does not divide the polynomial. Any reducible quartic
without a linear factor is a product of two irreducible
quadratics. The only possible quadratic factor has just been
excluded, so the quartic is irreducible.
:::

<1>6. No other cases are irreducible, proving part (d).

::: proof
If $f$ is irreducible and $\alpha$ is a root, then
$[\mathbb F_p(\alpha):\mathbb F_p]=\deg f=p^n$.
Step <1>3 and the tower law imply
$$
p^n\mid np,\qquad\text{hence }p^{n-1}\mid n.
$$
For $n\geq3$, the inequality $2^{n-1}>n$ holds: it is true
at $n=3$, and doubling the left side preserves strict inequality
at the next integer since $2n\geq n+1$.
Then $p^{n-1}\geq2^{n-1}>n$, contradicting the divisibility.
Thus $n=1$ or $2$. In the latter case the divisibility gives
$p\mid2$, hence $p=2$.
Steps <1>4 and <1>5 establish irreducibility in both surviving
cases, completing every part.
:::
:::
