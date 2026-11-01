::: {.solution}
Let $p\colon X\to Y$ be a fibration with fibre $F$, let $(W,A)$ be a CW pair, let $g\colon W\to Y$ be a map, and let $f_0,f_1\colon W\to X$ be two lifts of $g$ with $f_0|_A=f_1|_A$.
Set $I=[0,1]$, let $\mathrm{pr}_W\colon W\times I\to W$ be the projection, put $G=g\circ \mathrm{pr}_W$, and set

$$
B=(W\times\{0\})\cup(A\times I)\cup(W\times\{1\})\subset W\times I .
$$

For $n\ge 1$ the coefficient system written $\pi_nF$ in $H^k(W,A;\pi_nF)$ is the local system on $W$ given by the action of $\pi_1(W)$ on $\pi_nF$ (Hatcher, Exercise 4.3.10; §3.H for cohomology with local coefficients). When that action is trivial these are ordinary cohomology groups with coefficients in the abelian group $\pi_nF$.

::: pf

::: {.pf-step #cylinder}
A homotopy rel $A$ from $f_0$ to $f_1$ all of whose levels are lifts of $g$ is the same thing as a solution of the relative lifting problem of Hatcher §4.3 for the CW pair $(W\times I,B)$, the fibration $p$, the map $G$, and the partial lift $h_0\colon B\to X$ of $G|_B$ given by
$$
h_0(w,0)=f_0(w),\qquad h_0(w,1)=f_1(w),\qquad h_0(a,t)=f_0(a)
$$
for $w\in W$, $a\in A$ and $t\in I$.

::: pf-proof
On $A\times\{0\}$ the first and the third formula both give $f_0(a)$, and on $A\times\{1\}$ the second gives $f_1(a)$ while the third gives $f_0(a)$, which is the same since $f_0|_A=f_1|_A$. The three closed sets $W\times\{0\}$, $A\times I$ and $W\times\{1\}$ cover $B$, so the pasting lemma makes $h_0$ a well-defined continuous map. It lifts $G|_B$: $p h_0(w,0)=p f_0(w)=g(w)=G(w,0)$ and $p h_0(w,1)=p f_1(w)=g(w)=G(w,1)$ because $f_0$ and $f_1$ lift $g$, and $p h_0(a,t)=p f_0(a)=g(a)=G(a,t)$.

A continuous $H\colon W\times I\to X$ with $pH=G$ and $H|_B=h_0$ gives the homotopy $H_t(w)=H(w,t)$, which satisfies $H_0=f_0$, $H_1=f_1$, $H_t(a)=h_0(a,t)=f_0(a)$ for $a\in A$ and $pH_t=g$. Conversely a homotopy $H_t$ rel $A$ from $f_0$ to $f_1$ through lifts of $g$ gives the continuous map $H(w,t)=H_t(w)$, which satisfies $pH=G$ and restricts to $h_0$ on $B$. The two passages are inverse to each other, both being the correspondence between a map on $W\times I$ and the family of its restrictions to the slices $W\times\{t\}$.
:::

:::

::: {.pf-step #cylinder-cells}
$(W\times I,B)$ is a CW pair, and its $(k+1)$-cells are exactly the cells $e^k\times(0,1)$ with $e^k$ a $k$-cell of $W$ not contained in $A$; hence they are in bijection with the $k$-cells of the relative CW complex $(W,A)$.

::: pf-proof
Let $I$ carry the cell structure with the two $0$-cells $\{0\}$ and $\{1\}$ joined by the $1$-cell $(0,1)$. By the product cell structure (Hatcher, Chapter 0, “Products” and “Suspension”) the cells of $W\times I$ are
$$
e^k\times\{0\},\qquad e^k\times\{1\},\qquad e^k\times(0,1)
$$
for the cells $e^k$ of $W$. The product topology on $W\times I$ and its topology as this cell complex coincide, because $I$ has finitely many cells, so this is a CW structure on the space $W\times I$.

The subspaces $W\times\{0\}$ and $W\times\{1\}$ are subcomplexes, with cells $e^k\times\{0\}$ and $e^k\times\{1\}$, and $A\times I$ is a subcomplex, with cells $e^k\times\{0\}$, $e^k\times\{1\}$ and $e^k\times(0,1)$ for the cells $e^k$ lying in $A$. A union of subcomplexes is a subcomplex, so $B$ is one and its cells are exactly the cells listed. The cells of $W\times I$ that are not cells of $B$ are therefore the cells $e^k\times(0,1)$ of dimension $k+1$ with $e^k$ not contained in $A$, and these are indexed by the $k$-cells of $(W,A)$.
:::

:::

::: {.pf-step #relative-obstructions}
Assume that $p\colon X\to Y$ has a Moore–Postnikov tower of principal fibrations; by Theorem 4.71 this holds as soon as $\pi_1(X)$ acts trivially on $\pi_n(M_p,X)$ for all $n>1$, where $M_p$ is the mapping cylinder of $p$. Then the relative lifting problem of step [](#cylinder) has, for each $n\ge 1$, an obstruction class
$$
\omega_n\in H^{n+1}(W\times I,B;\pi_nF)
$$
which is defined once a lift over $Z_{n-1}$ has been chosen and $\omega_1,\dots,\omega_{n-1}$ vanish, $\pi_1F$ being required to be abelian when $n=1$; and the problem has a solution if and only if some compatible choice of the successive lifts makes every $\omega_n$ vanish.

::: pf-proof
In such a tower each $Z_{n+1}\to Z_n$ is a principal fibration with fibre $K(\pi_nF,n)$, so $Z_{n+1}$ is the pullback of the path fibration over $K(\pi_nF,n+1)$ along a map $k_n\colon Z_n\to K(\pi_nF,n+1)$, and a lift of $W\times I$ to $Z_{n+1}$ over a given lift to $Z_n$ amounts to a nullhomotopy of the composite $W\times I\to Z_n\to K(\pi_nF,n+1)$. That nullhomotopy is prescribed on $B$; the composite together with the prescribed nullhomotopy is a map $W\times I\cup CB\to K(\pi_nF,n+1)$, and since this target is a $K(\pi_nF,n+1)$ the homotopy class of such a map relative to $CB$ is an element
$$
\omega_n\in H^{n+1}(W\times I\cup CB,CB;\pi_nF)\cong H^{n+1}(W\times I,B;\pi_nF),
$$
by Theorem 4.57 with local coefficients as in §3.H and excision for the pair $(W\times I\cup CB,CB)$. This is the construction that Hatcher carries out in §4.3 (“Obstruction Theory”, the paragraph preceding Proposition 4.72) for the extension problem, and Proposition 4.72 states that a lift $W\times I\to Z_n$ extending the given lift on $B$ exists if and only if $\omega_n=0$. Iterating over $n$ produces the sequence of classes, each defined only after the previous ones are killed and a lift to the previous stage is chosen. For the relative lifting problem Hatcher states the outcome in §4.3 (the paragraph following Proposition 4.72): “Having a lift to $Z_1$, the analysis proceeds exactly as before. One finds a sequence of obstructions $\omega_n\in H^{n+1}(W,A;\pi_nF)$, assuming $\pi_1F$ is abelian in the case $n=1$. A lift to $X$ exists, extending the given lift on $A$, if each successive $\omega_n$ is zero.” That is the statement used here, with the pair $(W\times I,B)$ in place of $(W,A)$.

Conversely, if a lift $W\times I\to X$ extending $h_0$ exists, then composing it with $X\to Z_n$ gives a lift to $Z_n$ extending the given lift on $B$ (the maps of the tower are compatible by construction), so $\omega_n=0$ for the successive choices of lifts that this solution determines, again by Proposition 4.72. The preliminary stage of the tower, the lift to the covering space $Z_1$, is a covering-space question that Hatcher treats separately just before the quoted passage, noting that the choice of lift agreeing with the given one on the subspace can fail only when that subspace has more than one component; the classes $\omega_n$ are those of the stages $n\ge 1$ that follow it.
:::

:::

::: {.pf-step #cochain-shift}
For every abelian group $G$ and every $m\ge 0$ there is an isomorphism
$$
H^{m+1}(W\times I,B;G)\cong H^m(W,A;G),
$$
and it is natural in $G$; for coefficients in a local system on $W$, pulled back to $W\times I$, the same formula holds.

::: pf-proof

::: {.pf-step #cochain-groups}
For every $m\ge 0$ the formula
$$
c\longmapsto \tilde c,\qquad \tilde c(e^m)=c\big(e^m\times(0,1)\big)
$$
defines an isomorphism of groups $C^{m+1}(W\times I,B;G)\to C^m(W,A;G)$.

::: pf-proof
By step [](#cylinder-cells) the $(m+1)$-cells of $(W\times I,B)$ are the cells $e^m\times(0,1)$ for the $m$-cells $e^m$ of $W$ not in $A$, and the $m$-cells of $(W,A)$ are exactly those cells $e^m$. A relative cellular cochain group is the direct sum of one copy of $G$ for each relative cell, so the two groups are free on the same index set and the displayed assignment, which matches the cell $e^m\times(0,1)$ with the cell $e^m$, is an isomorphism.
:::

:::

::: {.pf-step #cochain-differentials}
The isomorphism of step [](#cochain-groups) carries the coboundary of $(W\times I,B)$ to the coboundary of $(W,A)$: for every $c\in C^{m+1}(W\times I,B;G)$ and every $m$-cell $e^m$ of $W$ not in $A$,
$$
\big\langle \delta c,\,e^m\times(0,1)\big\rangle=\big\langle \delta\tilde c,\,e^m\big\rangle .
$$

::: pf-proof
The cellular boundary formula for a product cell (Hatcher, §3.B, “The Cross Product in Homology”) gives, for the $1$-cell $(0,1)$ of $I$ with $d(0,1)=\{1\}-\{0\}$,
$$
d\big(e^m\times(0,1)\big)=de^m\times(0,1)+(-1)^m e^m\times\big(\{1\}-\{0\}\big).
$$
The cells $e^m\times\{0\}$ and $e^m\times\{1\}$ lie in $B$, so a relative cochain, extended by zero on the cells of $B$, takes the value $0$ on those two terms. Hence
$$
\big\langle \delta c,\,e^m\times(0,1)\big\rangle=\big\langle c,\,d(e^m\times(0,1))\big\rangle=\big\langle c,\,de^m\times(0,1)\big\rangle=\big\langle \tilde c,\,de^m\big\rangle=\big\langle \delta\tilde c,\,e^m\big\rangle,
$$
where the third equality expands $de^m$ in the cells $e^{m-1}$ of $W$ and applies the definition of $\tilde c$ to each term, and the first and last equalities are the definition of the coboundary as the dual of the boundary.
:::

:::

::: {.pf-step #cochain-computes}
For a CW pair $(Z,C)$ the cohomology of the relative cellular cochain complex $C^{*}(Z,C;G)$ is the singular cohomology $H^{*}(Z,C;G)$.

::: pf-proof
The relative cellular chain complex is free, and its homology is the singular homology of the pair: the cells of the quotient CW complex $Z/C$ are the cells of $Z$ that are not in $C$, its cellular chain complex is thus the relative one, and its homology is $H_*(Z/C)\cong H_*(Z,C)$ by Theorem 2.35 and Proposition 2.22. Theorem 3.2 then computes the cohomology of the dual of a free chain complex from its homology by the universal coefficient formula, which applied to the relative cellular chain complex and to the singular chain complex of the pair gives the same group $\operatorname{Hom}(H_n(Z,C),G)\oplus \operatorname{Ext}(H_{n-1}(Z,C),G)$ in both cases.
:::

:::

:::

:::

::: pf-qed
By step [](#relative-obstructions) the obstruction classes of the successive stages of the relative lifting problem attached to the two lifts are classes
$$
\omega_n\in H^{n+1}(W\times I,B;\pi_nF),\qquad n\ge 1,
$$
and by step [](#cochain-shift) with $m=n$, coefficients in the local system $\pi_nF$, each of these groups is isomorphic to $H^n(W,A;\pi_nF)$. Transporting the classes across that isomorphism places the $n$-th obstruction to a homotopy rel $A$ from $f_0$ to $f_1$ through lifts of $g$ in $H^n(W,A;\pi_nF)$, for $n\ge 1$, with $\pi_1F$ abelian when $n=1$. By step [](#cylinder) such a homotopy is exactly a solution of that lifting problem, so the classes $\omega_n$ can be made to vanish successively precisely when the homotopy exists, and, as Hatcher notes in the paragraphs following Proposition 4.72, the class at stage $n$ depends on the choices of the earlier lifts, so what is located in each group is the class of that stage and not one intrinsic class attached to the pair of lifts.
:::

:::

:::
