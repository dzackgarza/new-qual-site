---
schema: qual/card@1
id: P-RAF23E
kind: problem
title: "Parallelogram law implies Hilbert space"
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
  date: 2026-09-08
  note: Checked against Problem 5 of the official UCSD Fall 2023 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $(X, \|\cdot\|)$ be a complex Banach space satisfying: $\|x + y\|^2 + \|x - y\|^2 = 2\|x\|^2 + 2\|y\|^2$.
Prove that the space is a Hilbert space and the norm is induced by the inner product.
Namely you need to construct an inner product $(\cdot, \cdot)$ on $X$ such that its induced norm is the same as $\|\cdot\|$.
:::

::: solution
<1>1. Construct the underlying real bilinear form.
::: proof
Write
\[
q(x):=\|x\|^2
\]
and define, viewing $X$ first as a real vector space,
\[
B(x,y):=\frac14\bigl(q(x+y)-q(x-y)\bigr).
\]
Clearly $B(x,y)=B(y,x)$ and
\[
B(x,x)=q(x)=\|x\|^2.
\]

We prove additivity in the first variable. Applying the parallelogram identity to $(x+y,z)$ and to $(x-y,z)$ gives
\[
\begin{aligned}
&q(x+y+z)+q(x+y-z)=2q(x+y)+2q(z),\\
&q(x-y+z)+q(x-y-z)=2q(x-y)+2q(z).
\end{aligned}
\]
Subtracting yields
\[
B(x+z,y)+B(x-z,y)=2B(x,y).
\]
Putting $z=x$ gives
\[
B(2x,y)=2B(x,y).
\]
Now replace $x,z$ by
\[
x=\frac{u+v}{2},
\qquad
z=\frac{u-v}{2}.
\]
Then
\[
B(u,y)+B(v,y)
=2B\!\left(\frac{u+v}{2},y\right)
=B(u+v,y).
\]
Thus $B$ is additive in its first variable. Symmetry gives additivity in the second variable.

Integer and rational homogeneity follow from additivity. Since $B$ is continuous—indeed
\[
|B(x,y)|
\le \frac14\bigl(\|x+y\|^2+\|x-y\|^2\bigr)
=\frac12(\|x\|^2+\|y\|^2)
\]
and the defining expression is continuous—rational homogeneity extends to real homogeneity. Hence $B$ is a symmetric real-bilinear form satisfying
\[
B(x,x)=\|x\|^2.
\]
In particular $B$ is a real inner product on the underlying real vector space.
:::

<1>2. Record how multiplication by $i$ interacts with $B$.
::: proof
Because the norm is a complex norm,
\[
q(ix)=\|ix\|^2=\|x\|^2=q(x).
\]
Therefore, using the real polarization formula,
\[
\begin{aligned}
B(ix,iy)
&=\frac14\bigl(q(i(x+y))-q(i(x-y))\bigr)\\
&=\frac14\bigl(q(x+y)-q(x-y)\bigr)\\
&=B(x,y).
\end{aligned}
\]
Consequently
\[
B(ix,y)
=B(ix,i(-iy))
=B(x,-iy)
=-B(x,iy).
\]
:::

<1>3. Build the complex inner product.
::: proof
Define
\[
\langle x,y\rangle
:=B(x,y)-iB(ix,y).
\]
Since $B$ is real bilinear, $\langle\cdot,y\rangle$ is additive. Moreover
\[
\begin{aligned}
\langle ix,y\rangle
&=B(ix,y)-iB(i(ix),y)\\
&=B(ix,y)+iB(x,y)\\
&=i\langle x,y\rangle.
\end{aligned}
\]
Together with real homogeneity, this proves complex linearity in the first variable.

Using symmetry of $B$ and Step 2,
\[
\begin{aligned}
\langle y,x\rangle
&=B(x,y)-iB(iy,x)\\
&=B(x,y)-iB(x,iy)\\
&=B(x,y)+iB(ix,y)\\
&=\overline{\langle x,y\rangle}.
\end{aligned}
\]
Thus the form is conjugate symmetric and hence conjugate linear in the second variable.

Finally,
\[
\langle x,x\rangle
=B(x,x)-iB(ix,x).
\]
But Step 2 gives
\[
B(ix,x)=-B(x,ix)=-B(ix,x),
\]
so $B(ix,x)=0$. Hence
\[
\langle x,x\rangle=B(x,x)=\|x\|^2.
\]
Therefore $\langle\cdot,\cdot\rangle$ is an inner product whose induced norm is exactly the given norm.
:::

<1>4. Conclude completeness.
::: proof
The original normed space $X$ is Banach by hypothesis, and the norm induced by the constructed inner product is the original norm. Hence $X$ is complete for the inner-product norm. Therefore
\[
\boxed{X\text{ is a Hilbert space}.}
\]
:::
:::
