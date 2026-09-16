---
schema: qual/card@1
id: E-QVJ8J
kind: problem
title: Countability of the fundamental group under countable basis and regularity
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

::: {.exercise}

Prove the following.

Theorem.
Let $X$ be a space that is path connected, locally path connected, and semilocally simply connected.
If $X$ is regular with a countable basis, then $\pi_1(X, x_0)$ is countable.

Let $\mathcal{A}$ be a covering of $X$ by path-connected open sets such that for each $A \in \mathcal{A}$ and each $a \in A$, the homomorphism $\pi_1(A, a) \to \pi_1(X, a)$ induced by inclusion is trivial.
Let $\mathcal{B}$ be a countable open covering of $X$ by nonempty path-connected sets that satisfies the conditions of [[E-8Q9TN]]. Choose a point $p(B) \in B$ for each $B \in \mathcal{B}$.
For each pair $B$, $B'$ of elements of $\mathcal{B}$ for which $B \cap B' \neq \varnothing$, choose a path $g(B, B')$ in $B \cup B'$ from $p(B)$ to $p(B')$.
We call the path $g(B, B')$ a select path.

Let $B_0$ be a fixed element of $\mathcal{B}$; let $x_0 = p(B_0)$.
Show that if $f$ is a loop in $X$ based at $x_0$, then $f$ is path homotopic to a product of select paths, as follows:

(a) Show that there is a subdivision

$$
0 = t_0 < \dots < t_n = 1
$$

of $[0, 1]$ such that $f$ maps $[t_{n-1}, t_n]$ into $B_0$, and for each $i = 1, \ldots, n-1$, $f$ maps $[t_{i-1}, t_i]$ into an element $B_i$ of $\mathcal{B}$.
Set $B_n = B_0$.

(b) Let $f_i$ be the positive linear map of $[0, 1]$ onto $[t_{i-1}, t_i]$ followed by $f$.
Let $g_i = g(B_{i-1}, B_i)$.
Choose a path $\alpha_i$ in $B_i$ from $f(t_i)$ to $p(B_i)$; if $i = 0$ or $n$, let $\alpha_i$ be the constant path at $x_0$.
Show that

$$
[f_i] * [\alpha_i] = [\alpha_{i-1}] * [g_i].
$$

(c) Show that $[f] = [g_1] * \dots * [g_n]$.
:::

::: {.solution}
Let \(\mathcal A\) and the countable star-fine path-connected cover \(\mathcal B\) be as in the statement. Thus whenever \(B,B'\in\mathcal B\) intersect, there is \(A\in\mathcal A\) with
\[
B\cup B'\subset A,
\]
and every loop in \(A\) maps trivially in \(\pi_1(X)\).

(a) The sets \(f^{-1}(B)\), \(B\in\mathcal B\), form an open cover of the compact interval \([0,1]\). By the Lebesgue-number/subdivision lemma, there is a subdivision
\[
0=t_0<\cdots<t_n=1
\]
such that each \(f([t_{i-1},t_i])\) lies in some \(B_i\in\mathcal B\). Since \(f(1)=x_0\in B_0\) and \(B_0\) is open, refine the subdivision near \(1\) so that the last interval maps into \(B_0\); set \(B_n=B_0\). Consecutive \(B_{i-1}\) and \(B_i\) intersect because both contain \(f(t_{i-1})\) after the evident index shift (equivalently choose each \(B_i\) around the common subdivision point during refinement).

(b) The paths
\[
f_i*\alpha_i
\qquad\text{and}\qquad
\alpha_{i-1}*g_i
\]
have the same initial point \(f(t_{i-1})\) and terminal point \(p(B_i)\). Their concatenation with one reversed is a loop contained in
\[
B_{i-1}\cup B_i.
\]
Because \(B_{i-1}\cap B_i\ne\varnothing\), this union lies in some \(A\in\mathcal A\). The inclusion-induced map \(\pi_1(A)\to\pi_1(X)\) is trivial, so the loop is nullhomotopic in \(X\). Hence the two paths are homotopic rel endpoints:
\[
[f_i]*[\alpha_i]=[\alpha_{i-1}]*[g_i].
\]

(c) Rearranging the equality from (b),
\[
[f_i]=[\alpha_{i-1}]*[g_i]*[\alpha_i]^{-1}.
\]
Multiplying these identities for \(i=1,\dots,n\), all intermediate \(\alpha_i\)'s cancel. Since \(\alpha_0\) and \(\alpha_n\) are constant at \(x_0\),
\[
[f]=[f_1]*\cdots*[f_n]
=[g_1]*\cdots*[g_n].
\]
There are only countably many select paths because \(\mathcal B\) is countable, and the set of all finite words in a countable alphabet is countable. Every element of \(\pi_1(X,x_0)\) is represented by such a finite product. Therefore
\[
\boxed{\pi_1(X,x_0)\text{ is countable}.}
\]
:::
