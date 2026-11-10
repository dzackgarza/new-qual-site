---
schema: qual/card@1
id: P-AGH49PROJBIR
kind: problem
title: Projection from a general point is birational onto its image
classification:
  areas:
  - algebraic-geometry
  topics:
  - Birational Geometry
  - Projective Varieties
  - Morphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the statement and required references with the retained Hartshorne I.4.9 transcription. The proof uses a separating transcendence basis and a primitive element to choose a general linear coordinate system in which the last coordinate is unnecessary for the function field, while the projection center lies off X.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a projective variety of dimension $r$ in $\PP^n$, with $n \geq r + 2$.
Show that for a suitable choice of a point $P \notin X$ and a linear subspace $\PP^{n-1} \subseteq \PP^n$, the projection from $P$ to $\PP^{n-1}$ (Ex. I.3.14) induces a birational morphism of $X$ onto its image $X' \subseteq \PP^{n-1}$.
You will need to use Theorem I.4.6A, Theorem I.4.7A and Theorem I.4.8A.
This shows in particular that the birational map of Proposition I.4.9 can be obtained by a finite number of such projections.
:::

::: {.solution}
Let $K=K(X)$ be the function field of $X$.
Since $k$ is algebraically closed, hence perfect, $K$ is separably generated over $k$ [@Har77, Theorem I.4.8A].

::: pf

::: {.pf-step #s1}

There are homogeneous coordinates $x_0,\ldots,x_n$ on $\PP^n$ such that $X \not\subseteq Z(x_0)$ and none of the coordinate points $e_1,\ldots,e_n$ lies on $X$.

::: pf-proof

The hyperplanes of $\PP^n$ have empty common intersection, so some hyperplane $H$ does not contain $X$.
Then $X \intersect H$ is a proper closed subset of $H \cong \PP^{n-1}$.
Choose $e_1 \in H \sm X$, and inductively choose $e_j \in H$ outside $X$ and outside the linear span of $e_1,\ldots,e_{j-1}$, for $j \le n$.
Each choice is possible because $H$ is irreducible and the two excluded sets are proper closed subsets of $H$.
The points $e_1,\ldots,e_n$ are linearly independent and span $H$.
Take $x_0$ to be a linear form with $Z(x_0) = H$, extend to coordinates $x_0,\ldots,x_n$ dual to a basis $e_0, e_1, \ldots, e_n$ with $e_0 \notin H$.
Then $e_1,\ldots,e_n$ are the coordinate points and $X \not\subseteq Z(x_0)$.

:::

:::

::: {.pf-step #s2}

After renumbering $x_1,\ldots,x_n$, the functions $y_i = x_i/x_0$ satisfy: $y_1,\ldots,y_r$ is a separating transcendence basis of $K/k$, and $K$ is finite separable over $F = k(y_1,\ldots,y_r)$.

::: pf-proof

On the dense open set $X \intersect D_+(x_0)$ the functions $y_1,\ldots,y_n$ generate $K$ over $k$.
By [@Har77, Theorem I.4.7A], a separating transcendence basis can be chosen from this generating set; it has $r$ elements because $\trdeg_k K = \dim X = r$.
Renumbering $x_1,\ldots,x_n$ permutes $e_1,\ldots,e_n$, so step [](#s1){.pf-ref} still holds.
Then $K = F(y_{r+1},\ldots,y_n)$ is finite and separable over $F$.

:::

:::

::: {.pf-step #s3}

For all but finitely many $c \in k$, the element $z_c = y_{n-1} + c\, y_n$ satisfies $F(y_{n-1}, y_n) = F(z_c)$.

::: pf-proof

Because $n \ge r+2$, the indices $n-1$ and $n$ are both at least $r+1$, so $y_{n-1}$ and $y_n$ are separable over $F$.
Let $L$ be a normal closure of $K/F$, let $\beta_1,\ldots,\beta_p$ be the conjugates of $y_{n-1}$ in $L$, and let $\gamma_1,\ldots,\gamma_q$ be the conjugates of $y_n$, with $\gamma_1 = y_n$ and $\beta_1 = y_{n-1}$; the $\gamma_j$ are distinct by separability.
Exclude the finitely many $c \in k$ with $\beta_i + c \gamma_j = \beta_1 + c \gamma_1$ for some $i$ and some $j \neq 1$.
For any other $c$, let $g$ and $f$ be the minimal polynomials of $y_n$ and $y_{n-1}$ over $F$, and put $h(T) = f(z_c - cT)$. Then $g$ and $h$ both lie in $F(z_c)[T]$ and have $y_n$ as their only common root in $L$.
Since $g$ has distinct roots, their greatest common divisor over $F(z_c)$ is $T - y_n$, so $y_n \in F(z_c)$, and then $y_{n-1} = z_c - c\, y_n \in F(z_c)$.
This is the standard proof of the primitive element theorem [@Har77, Theorem I.4.6A]; the excluded set is finite and $k$ is infinite.

:::

:::

::: {.pf-step #s4}

Choose $c$ as in step [](#s3){.pf-ref} with
$$
P = [0 : \cdots : 0 : -c : 1] \notin X .
$$
Then projection from $P$ to the hyperplane $Z(x_n) \cong \PP^{n-1}$ restricts to a morphism $\pi : X \to X' \coloneqq \overline{\pi(X)}$.

::: pf-proof

The points $P$ lie on the line $\ell = Z(x_0,\ldots,x_{n-2})$ through $e_{n-1}$ and $e_n$.
By step [](#s1){.pf-ref}, $e_n \notin X$, so $\ell \not\subseteq X$, and $X \intersect \ell$ is a proper closed subset of $\ell \cong \PP^1$, hence finite.
So all but finitely many $c$ give $P \notin X$, and a $c$ meeting both conditions exists.

The point $P$ is the only common zero of the linear forms $x_0, \ldots, x_{n-2}, x_{n-1} + c\, x_n$, and $P \notin Z(x_n)$.
By Ex. I.3.14, projection from $P$ to $Z(x_n)$ is
$$
[x_0 : \cdots : x_n] \longmapsto [x_0 : \cdots : x_{n-2} : x_{n-1} + c\, x_n : 0],
$$
a morphism on $\PP^n \sm \theset{P}$, hence on $X$.
The image of the irreducible space $X$ is irreducible, so $X'$ is a projective variety.

:::

:::

::: {.pf-step #s5}

The morphism $\pi : X \to X'$ is birational.

::: pf-proof

The morphism $\pi$ is dominant by the definition of $X'$, so it induces an inclusion $\pi^* : K(X') \hookrightarrow K$.
On $X \intersect D_+(x_0)$ the coordinate functions of $X'$ pull back to $y_1, \ldots, y_{n-2}, z_c$, so
$$
\pi^* K(X') = k(y_1, \ldots, y_{n-2}, z_c) = F(y_{r+1}, \ldots, y_{n-2}, z_c) .
$$
By step [](#s3){.pf-ref} this field contains $y_{n-1}$ and $y_n$, hence equals $F(y_{r+1},\ldots,y_n) = K$.
A dominant morphism inducing an isomorphism of function fields is birational [@Har77, Corollary I.4.5].

:::

:::

::: {.pf-step #s6}

Repeating the construction reduces the ambient projective dimension to $r+1$.

::: pf-proof

The image $X'$ is birational to $X$, so it again has dimension $r$.
While the ambient dimension $m$ satisfies $m \ge r+2$, step [](#s5){.pf-ref} replaces the variety birationally by one in $\PP^{m-1}$.
After finitely many repetitions the image lies in $\PP^{r+1}$, where an $r$-dimensional projective variety is a hypersurface by [[P-AGH28HYPERSURFACE]].
The composite is birational, which gives the final assertion of the statement.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} to [](#s5){.pf-ref} construct the point $P$, the hyperplane $Z(x_n)$, and the birational projection; step [](#s6){.pf-ref} gives the finite iteration.

:::

:::
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 4.9, PDF p. 6: take $X$ affine in $\AA^n$ with coordinates $x_1,\ldots,x_n$, choose a separating transcendence basis $x_1,\ldots,x_r$ by Theorems 4.7A and 4.8A, write $K(X)$ as generated by $a_{r+1}x_{r+1}+\cdots+a_nx_n$ by Theorem 4.6A, pick a form $b_{r+1}x_{r+1}+\cdots+b_nx_n$ not proportional to it, and project from a point outside $X$ and outside that plane.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), gives no solution to 4.9.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.4.9, PDF p. 42: a linear space disjoint from $X$ gives a surjective projection to $\PP^r$ and hence an injection $k(X)\hookrightarrow k(\PP^r)$; then $k(X)$ is a finite algebraic extension of $k(\PP^r)$ generated by $x_{r+1},\ldots,x_n$, and the primitive element theorem produces a single generator $\sum a_ix_i$, so that $k(\PP^r)\hookrightarrow k(Z(F))\cong k(X)$ for $F$ the minimal polynomial, giving an open set on which the projection is one-to-one.
Borcherds' construction leaves the point $P$ implicit — his linear form produces a projection to $\PP^{n-1}$, not the choice of centre — while Egbert projects all the way down to $\PP^r$ in one step. The proof above chooses the centre $[0:\cdots:0:-c:1]$ explicitly, excludes the finitely many bad $c$ so that $P\notin X$, writes the projection as $[x_0:\cdots:x_n]\mapsto[x_0:\cdots:x_{n-2}:x_{n-1}+cx_n:0]$, and iterates to reach $\PP^{r+1}$, which is the final assertion of the exercise.
Agree with Borcherds; the centre is made explicit here.
:::
