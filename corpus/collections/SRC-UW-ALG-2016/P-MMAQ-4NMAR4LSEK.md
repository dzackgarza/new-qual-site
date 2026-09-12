---
schema: qual/card@1
id: P-MMAQ-4NMAR4LSEK
kind: problem
title: Galois group of $x^5-5a^4x+a$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Polynomials
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $a\in\mathbb N$, $a>0$.
Compute the Galois group of the splitting field of the polynomial $x^5-5a^4x+a$ over $\mathbb Q$.
:::


::: solution
Let
\[
f(x)=x^5-5a^4x+a,
\qquad a\in\mathbb N,\ a>0.
\]

<1>1. The polynomial \(f\) has no rational root.
::: {.proof}
Since \(f\) is monic with integer coefficients, any rational root is an integer \(r\) dividing \(a\). Thus \(0<|r|\le a\).

If \(r>0\), then \(r^5\le a^4r\), so
\[
f(r)=r^5-5a^4r+a
\le -4a^4r+a<0.
\]
If \(r<0\), write \(r=-s\) with \(1\le s\le a\). Then
\[
f(-s)=-s^5+5a^4s+a
\ge4a^4s+a>0.
\]
Hence no integer, and therefore no rational, root exists.
:::

<1>2. The polynomial \(f\) has no quadratic factor over \(\mathbb Q\).
::: {.proof}
By Gauss's lemma, if \(f\) had a quadratic factor over \(\mathbb Q\), it would factor in \(\mathbb Z[x]\) as
\[
f(x)=(x^2+ux+v)(x^3+cx^2+dx+e),
\]
with \(u,v,c,d,e\in\mathbb Z\). Comparing the coefficients of \(x^4,x^3,x^2\) gives
\[
c=-u,
\qquad
d=u^2-v,
\qquad
e=2uv-u^3=u(2v-u^2).
\]
Comparing the constant and linear coefficients then gives
\[
uv(2v-u^2)=a
\tag{1}
\]
and
\[
3u^2v-u^4-v^2=-5a^4,
\]
or equivalently
\[
u^4-3u^2v+v^2=5a^4.
\tag{2}
\]

Equation (1) shows that the nonzero integers \(u\), \(v\), and \(2v-u^2\) all divide \(a\). Hence
\[
|u|\le a,
\qquad |v|\le a.
\]
If \(a>1\), then
\[
|u^4-3u^2v+v^2|
\le a^4+3a^3+a^2
<5a^4,
\]
because
\[
5a^4-(a^4+3a^3+a^2)
=a^2(4a+1)(a-1)>0.
\]
This contradicts (2).

If \(a=1\), equation (1) forces \(u,v,2v-u^2\in\{\pm1\}\). Since \(u^2=1\), the condition \(2v-u^2=\pm1\) forces \(v=1\), then (1) forces \(u=1\). But the left side of (2) is then
\[
1-3+1=-1\ne5.
\]
So no quadratic factor exists in this case either.
:::

<1>3. The polynomial \(f\) is irreducible over \(\mathbb Q\).
::: {.proof}
A reducible quintic has a factor of degree \(1\) or \(2\): if the degrees of two nonconstant factors sum to \(5\), the smaller degree is at most \(2\). Steps <1>1 and <1>2 exclude both possibilities. Hence \(f\) is irreducible.
:::

<1>4. The polynomial \(f\) has exactly three real roots.
::: {.proof}
Its derivative is
\[
f'(x)=5(x^4-a^4).
\]
Thus \(f\) is strictly increasing on \(( -\infty,-a)\), strictly decreasing on \((-a,a)\), and strictly increasing on \((a,\infty)\). Moreover
\[
f(-a)=4a^5+a>0,
\qquad
f(a)=a-4a^5<0,
\]
and
\[
\lim_{x\to-\infty}f(x)=-\infty,
\qquad
\lim_{x\to\infty}f(x)=\infty.
\]
The intermediate value theorem and strict monotonicity therefore give exactly one real root in each of
\[
(-\infty,-a),
\qquad(-a,a),
\qquad(a,\infty).
\]
Hence exactly three roots are real, and the remaining two form one nonreal complex-conjugate pair.
:::

<1>5. Let \(E\) be the splitting field and \(G=\operatorname{Gal}(E/\mathbb Q)\). Then \(G\) is a transitive subgroup of \(S_5\) containing a transposition.
::: {.proof}
Irreducibility from <1>3 implies that \(G\) acts transitively on the five roots. By <1>4, complex conjugation fixes the three real roots and exchanges the two nonreal roots, so its permutation on the roots is a transposition.
:::

<1>6. A transitive subgroup \(H\le S_5\) containing a transposition is all of \(S_5\).
::: {.proof}
Let \(\tau\in H\) be a transposition. Form a graph whose vertices are the five letters and whose edges are the supports of the conjugates
\[
h\tau h^{-1},
\qquad h\in H.
\]
This graph has at least one edge and is \(H\)-invariant. Since \(H\) is transitive on the five vertices, all connected components have the same size. Because \(5\) is prime and an edge exists, the graph must be connected.

The transpositions corresponding to the edges of any connected graph generate the full symmetric group on its vertices. Hence the conjugates of \(\tau\) generate \(S_5\). Since all those conjugates lie in \(H\), we have \(S_5\le H\), so \(H=S_5\).
:::

<1>7. Therefore
\[
\boxed{\operatorname{Gal}(E/\mathbb Q)\cong S_5}.
\]
::: {.proof}
Apply <1>6 to the group in <1>5.
:::
:::
