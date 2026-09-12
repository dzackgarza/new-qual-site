---
schema: qual/card@1
id: P-C8XMR
kind: problem
title: Elements of a Galois extension of degree $2^n$ are constructible; a root of
  an irreducible quartic with splitting-field degree $24$ is not
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both assertions, including Galoisness and the splitting-field degree 24, with Summer 2007 Fields 3 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the complex constructibility convention, the index-two subgroup chain, and the explicit Galois enclosure of a quadratic tower before using the degree obstruction."
---

::: problem
a. Suppose that $K$ is a Galois extension of $\mathbb{Q}$ of dimension $2^n$ for some positive integer $n$.
Prove that every element of $K$ is constructible.

b. Suppose $f(x) \in \mathbb{Q}[x]$ is an irreducible quartic such that the splitting field of $f(x)$ over $\mathbb{Q}$ has dimension 24. Suppose $\alpha$ is a root of $f(x)$.
Prove that $\alpha$ is not constructible.
:::

::: solution
View the number fields inside $\mathbb C$. A complex number is
constructible when its real and imaginary coordinates are
straightedge-and-compass constructible from $0$ and $1$.

<1>1. A complex number $z$ is constructible if and only if it lies
in a finite tower
$$
\mathbb Q=E_0\subset E_1\subset\cdots\subset E_r\subseteq\mathbb C,
\qquad [E_i:E_{i-1}]=2.
$$
The tower of length zero is allowed.

::: proof
Use the real quadratic-tower criterion and the fact that the real
constructible numbers form a field closed under nonnegative square
roots [@DF04]. For constructible real and imaginary coordinates,
combine their two real quadratic towers and adjoin $i$.
Each adjunction still has degree at most $2$ after the earlier fields
are enlarged; omit any degree-$1$ steps. This gives a quadratic
tower containing $z$.

Conversely, complex numbers with constructible coordinates form a
field, by the coordinate formulas for addition, multiplication,
and division. This field is also closed under taking square roots.
Indeed, for $z=a+ib$ with constructible real $a,b$, put
$$
s=\sqrt{a^2+b^2},\qquad
u=\sqrt{\frac{s+a}{2}},\qquad
v=\sqrt{\frac{s-a}{2}}.
$$
All radicands are nonnegative, and all three numbers are constructible.
We have $u^2-v^2=a$ and $2uv=|b|$. Choose
$\varepsilon\in\{1,-1\}$ with $\varepsilon|b|=b$; either sign is
allowed when $b=0$. Then $(u+i\varepsilon v)^2=z$.
The quadratic formula now shows that every quadratic extension
of a field of constructible complex numbers still consists of
constructible numbers. Induction up the tower proves the converse.
:::

<1>2. A group of order $2^n$ admits a chain from the whole group
to the identity subgroup with every successive index equal to $2$.

::: proof
We induct on $n$, with the trivial group as the case $n=0$.
For a nontrivial $2$-group $G$, the conjugacy-class equation shows
that $|Z(G)|$ is even: every noncentral conjugacy class has size
$[G:C_G(g)]$, a power of $2$ greater than $1$.
Since the center contains the identity, it therefore contains some
$z\ne1$. By Lagrange's theorem $z$ has order $2^e$ for some $e\geq1$.
The element $z^{2^{e-1}}$ is central of order $2$; let $C$ be its
generated subgroup. Then $C\lhd G$ and $|G/C|=2^{n-1}$.

Apply induction to $G/C$. Taking inverse images of its subgroup
chain gives a chain from $G$ to $C$ with all successive indices $2$,
because the quotient map identifies the relevant coset spaces.
Append $C\supset\{1\}$ to obtain the required chain.
:::

<1>3. Part (a) follows from the Galois correspondence.

::: proof
The group $G=\operatorname{Gal}(K/\mathbb Q)$ has order $2^n$.
Choose the chain
$$
G=G_0\supset G_1\supset\cdots\supset G_n=\{1\}
$$
from step <1>2, and set $F_i=K^{G_i}$. The Galois correspondence
and its degree formula [@DF04] give
$$
\mathbb Q=F_0\subset F_1\subset\cdots\subset F_n=K,
\qquad [F_{i+1}:F_i]=[G_i:G_{i+1}]=2.
$$
Thus every element of $K$ lies in a quadratic tower and is
constructible by step <1>1.
:::

<1>4. Every finite quadratic tower over $\mathbb Q$ is contained
in a finite Galois extension of $\mathbb Q$ of power-of-two degree.

::: proof
Let $\mathbb Q=E_0\subset\cdots\subset E_r$ be such a tower.
In characteristic zero, completing the square in a quadratic
minimal polynomial gives
$$
E_i=E_{i-1}(\sqrt{a_i}),\qquad a_i\in E_{i-1}^{\times}.
$$
We construct finite Galois fields $N_i\supseteq E_i$ of
power-of-two degree over $\mathbb Q$, together with polynomials
$g_i\in\mathbb Q[T]$ having splitting field $N_i$.
Start with $N_0=\mathbb Q$ and $g_0(T)=T$.

Suppose $N_{i-1}$ and $g_{i-1}$ have been constructed, and put
$H=\operatorname{Gal}(N_{i-1}/\mathbb Q)$. Define
$$
q_i(T)=\prod_{\sigma\in H}(T^2-\sigma(a_i)),\qquad
N_i=N_{i-1}\bigl(\sqrt{\sigma(a_i)}:\sigma\in H\bigr).
$$
The coefficients of $q_i$ belong to $N_{i-1}$ and are fixed by $H$,
because each group element permutes the factors. Since the fixed
field of $H$ is $\mathbb Q$, we have $q_i\in\mathbb Q[T]$.
The field $N_i$ is precisely the splitting field of
$g_i=g_{i-1}q_i$: the roots of $g_{i-1}$ generate $N_{i-1}$,
and the additional roots are the two signs of each displayed
square root. Therefore $N_i/\mathbb Q$ is finite Galois.

There are finitely many square roots to adjoin. Each adjunction
has degree $1$ or $2$, so $[N_i:N_{i-1}]$ is a power of $2$.
The tower law makes $[N_i:\mathbb Q]$ a power of $2$ as well.
The identity element of $H$ ensures that $\sqrt{a_i}\in N_i$,
and hence $E_i\subseteq N_i$. This completes the induction;
$N_r$ is the required extension.
:::

<1>5. The root in part (b) is not constructible.

::: proof
Suppose $\alpha$ were constructible. Steps <1>1 and <1>4 put it in
a finite Galois extension $N/\mathbb Q$ with $[N:\mathbb Q]=2^m$
for some $m\geq0$. The irreducible polynomial $f$ has a root in
the normal extension $N/\mathbb Q$, so it splits in $N$.
Consequently its splitting field $L$ is contained in $N$.
The tower law would give
$$
24=[L:\mathbb Q]\mid[N:\mathbb Q]=2^m,
$$
which is impossible since $3\mid24$ but $3\nmid2^m$.
Thus $\alpha$ is not constructible.
:::
:::
