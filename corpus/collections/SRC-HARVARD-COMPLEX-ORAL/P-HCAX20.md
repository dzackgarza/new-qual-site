---
schema: qual/card@1
id: P-HCAX20
kind: problem
title: Argument principle as a winding-number statement
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Winding Number
relations: []
review: draft
---

::: problem
a. State the argument principle and explain its name.

b. Reformulate it without contour integrals as a statement about the winding number of an arbitrary continuous map from a domain to $\mathbb C$ with isolated zeros.
:::

::: solution
For the classical argument principle, let $f$ be meromorphic on a neighborhood of a positively oriented simple closed curve $\gamma$ and its interior, with no zeros or poles on $\gamma$. Then
\[
\frac{1}{2\pi i}\int_\gamma \frac{f'(z)}{f(z)}\,dz
=N-P,
\]
where $N$ and $P$ are the numbers of zeros and poles inside $\gamma$, counted with multiplicity.

Since $d\log f=f'/f\,dz$ wherever $f\ne0$, the integral measures the total change of a continuous argument of $f(\gamma(t))$. Equivalently,
\[
\operatorname{wind}(f\circ\gamma,0)=N-P.
\]
This is why it is called the argument principle: the zero-pole count is the net change of $\arg f$ along the boundary, divided by $2\pi$.

For the purely topological version, let $U\subset\mathbb C$ be a domain, let $f:U\to\mathbb C$ be continuous, and suppose the zeros of $f$ are isolated. Let $\gamma$ be a positively oriented Jordan curve whose image contains no zero of $f$, and suppose only finitely many zeros
\[
a_1,\dots,a_m
\]
lie in its interior. Choose pairwise disjoint small positively oriented circles $\gamma_j$ around the $a_j$, containing no other zero. Define the local index of $f$ at $a_j$ by
\[
\operatorname{ind}_{a_j}(f)
=\operatorname{wind}(f\circ\gamma_j,0).
\]
Then
\[
\boxed{
\operatorname{wind}(f\circ\gamma,0)
=\sum_{j=1}^m \operatorname{ind}_{a_j}(f).}
\]

Indeed, remove the small disks bounded by the $\gamma_j$ from the region inside $\gamma$. On the resulting region $f$ has no zeros, so
\[
\frac{f}{|f|}:\text{region}\longrightarrow S^1
\]
is continuous. The oriented boundary consists of $\gamma$ together with the circles $\gamma_j$ with the opposite orientation. The total degree of the restriction to this boundary is therefore zero, which gives exactly the displayed identity.

If $f$ is holomorphic, the local index at a zero of multiplicity $k$ is $k$: locally
\[
f(z)=(z-a)^k g(z),\qquad g(a)\ne0,
\]
and $g$ contributes zero winding on a sufficiently small circle. Thus the topological formula reduces to the usual argument principle when there are no poles; poles contribute negative local index for a meromorphic function.
:::
