---
schema: qual/card@1
id: P-RASP21E
kind: problem
title: "Intersection of L^2 balls with distance constraints"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 5 of the official UCSD Spring 2021 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Find all $f \in L^2([-1,1])$ such that
$$
\int_{-1}^{1} |f(x) - \sqrt{3}\,x|^2\,dx \leq \frac{1}{4}
$$
and
$$
\int_{-1}^{1} |f(x) - \sqrt{5}\,x^2|^2\,dx \leq \frac{9}{4}.
$$
:::


::: solution
Let
\[
u(x)=\sqrt3\,x,
\qquad
v(x)=\sqrt5\,x^2.
\]
Then
\[
\|u\|_2^2=3\int_{-1}^1x^2\,dx=2,
\qquad
\|v\|_2^2=5\int_{-1}^1x^4\,dx=2,
\]
and
\[
\langle u,v\rangle
=\sqrt{15}\int_{-1}^1x^3\,dx=0.
\]
Hence
\[
\|u-v\|_2^2=\|u\|_2^2+\|v\|_2^2=4,
\qquad
\|u-v\|_2=2.
\]

The two conditions on $f$ are
\[
\|f-u\|_2\le\frac12,
\qquad
\|f-v\|_2\le\frac32.
\]
By the triangle inequality,
\[
2=\|u-v\|_2
\le \|u-f\|_2+\|f-v\|_2
\le \frac12+\frac32=2.
\]
Thus equality holds everywhere. In particular,
\[
\|u-f\|_2=\frac12,
\qquad
\|f-v\|_2=\frac32,
\]
and equality holds in the triangle inequality for
\[
u-v=(u-f)+(f-v).
\]
In a Hilbert space, equality in the triangle inequality implies that $u-f$ and $f-v$ are nonnegative scalar multiples of one another. Hence $f$ lies on the line segment from $u$ to $v$.

Since $\|u-v\|_2=2$ and $\|f-u\|_2=1/2$, the point is one quarter of the way from $u$ to $v$:
\[
f=u+\frac14(v-u)=\frac34u+\frac14v.
\]
Therefore the unique solution is
\[
\boxed{
f(x)=\frac{3\sqrt3}{4}x+\frac{\sqrt5}{4}x^2
\quad\text{a.e. on }[-1,1].
}
\]
Indeed,
\[
\|f-u\|_2=\frac14\|v-u\|_2=\frac12,
\qquad
\|f-v\|_2=\frac34\|u-v\|_2=\frac32,
\]
so this function satisfies both inequalities with equality.
:::
