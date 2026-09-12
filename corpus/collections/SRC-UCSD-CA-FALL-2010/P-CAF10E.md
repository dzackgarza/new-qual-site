---
schema: qual/card@1
id: P-CAF10E
kind: problem
title: "Zeros of a polynomial in a sublevel set and Schwarz lemma-type inequality"
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Zeros of Polynomials
  - Schwarz Lemma
relations: []
review: draft
---

::: problem
Let $p(z)$ be a nonconstant polynomial and let $G$ be a connected component of the open set $\{z : |p(z)| < 1\}$.

(a) Show that $p(z)$ must have at least one zero in $G$.

(b) Let $f(z)$ be analytic in $G$, satisfying $|f(z)| \leq 1$ there.
Assume that $f(z)$ vanishes at every zero of $p(z)$ in $G$ and that the vanishing order of $f(z)$ at each such zero is at least that of $p(z)$.
Show that:

(i) $|f(z)| \leq |p(z)|$ in $G$.

(ii) If $a \in G$ is a zero of $p(z)$ of order $k$, then $|f^{(k)}(a)| \leq |p^{(k)}(a)|$.

Moreover, if for some such $a$ we have equality in (ii), then $f(z) = cp(z)$ for some unimodular constant $c$.
:::

::: solution
Because $p$ is a nonconstant polynomial, $|p(z)|\to\infty$ as
$|z|\to\infty$. Hence $\{|p|<1\}$, and therefore $G$, is bounded. Also
\[
\partial G\subset\{|p|=1\}.
\]
Indeed, a boundary point cannot satisfy $|p|<1$, since then it would lie in the
same open component as nearby points of $G$, and it cannot satisfy $|p|>1$ by
continuity.

For (a), suppose that $p$ has no zero in $G$. Then $1/p$ is holomorphic on $G$
and continuous on $\overline G$, because $p$ has no zero on $\partial G$ either.
On $\partial G$ we have $|1/p|=1$, while in $G$ we have $|1/p|>1$. This
contradicts the maximum modulus principle. Thus $p$ has at least one zero in
$G$.

For (b), define
\[
h(z)=\frac{f(z)}{p(z)}.
\]
At every zero of $p$ in $G$, the assumed vanishing-order inequality shows that
the apparent singularity of $h$ is removable. Hence $h$ extends holomorphically
to all of $G$.

Fix $0<r<1$. Every connected component $G_r$ of
\[
G\cap\{|p|<r\}
\]
is relatively compact in $G$, and on its boundary we have $|p|=r$. Therefore
\[
|h|=\frac{|f|}{|p|}\le \frac1r
\qquad\text{on }\partial G_r.
\]
By the maximum modulus principle, $|h|\le1/r$ throughout $G_r$. Given
$z\in G$, choose $r$ with $|p(z)|<r<1$ and let $G_r$ be the component containing
$z$. Then
\[
|h(z)|\le\frac1r.
\]
Letting $r\uparrow1$ gives $|h(z)|\le1$. Hence
\[
|f(z)|\le|p(z)|
\]
for all $z\in G$, proving (i).

Now let $a$ be a zero of $p$ of order $k$. Write
\[
p(z)=(z-a)^k q(z),\qquad q(a)\ne0,
\]
and similarly
\[
f(z)=(z-a)^k s(z)
\]
with $s$ holomorphic. Then $h(a)=s(a)/q(a)$, and
\[
p^{(k)}(a)=k!q(a),\qquad f^{(k)}(a)=k!s(a).
\]
Thus
\[
\left|\frac{f^{(k)}(a)}{p^{(k)}(a)}\right|=|h(a)|\le1,
\]
which is (ii).

If equality holds in (ii), then $|h(a)|=1$. Since $|h|\le1$ on the connected
domain $G$, the maximum modulus principle forces $h$ to be a constant $c$ with
$|c|=1$. Therefore $f=cp$ on $G$.
:::
