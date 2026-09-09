---
schema: qual/card@1
id: P-RASP15F
kind: problem
title: "Fourier transform from L^1 to C_0 is not onto"
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
  note: Checked against Problem 6 of the official UCSD Spring 2015 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $g_k = \chi_{[-1,1]} * \chi_{[-k,k]}$.
Here $f * g$ is the convolution of $f$ and $g$.

(i) Compute $\|g_k\|_{L^\infty}$.

(ii) Compute the inverse Fourier transform of $g_k$, namely $\mathcal{F}^{-1}(g_k)$.

(iii) Using the above computation show that the Fourier transform $\mathcal{F} : L^1(\mathbb{R}) \to C_0(\mathbb{R})$ is not onto.
Here $C_0(\mathbb{R})$ is the space of continuous functions which vanish at infinity.

Hint: Use the open mapping theorem.
:::

::: solution
<1>1. Compute $\|g_k\|_\infty$.
::: proof
For $x\in\mathbb R$,
\[
g_k(x)
=\int_{\mathbb R}\mathbf1_{[-1,1]}(x-y)\mathbf1_{[-k,k]}(y)\,dy.
\]
Thus $g_k(x)$ is the length of the intersection
\[
[-k,k]\cap[x-1,x+1].
\]
Since $k\ge1$, this length is at most $2$, and at $x=0$ it equals $2$. Therefore
\[
\boxed{\|g_k\|_\infty=2.}
\]
:::

<1>2. Compute the inverse Fourier transform.
::: proof
Use the convention
\[
\widehat f(\xi)=\int_{\mathbb R}e^{-2\pi ix\xi}f(x)\,dx.
\]
Then
\[
\mathcal F^{-1}(\mathbf1_{[-a,a]})(x)
=\int_{-a}^a e^{2\pi ix\xi}\,d\xi
=\frac{\sin(2\pi ax)}{\pi x},
\]
with the value at $x=0$ defined by continuity.

Since inverse Fourier transform converts convolution into pointwise product,
\[
\begin{aligned}
h_k(x):=\mathcal F^{-1}(g_k)(x)
&=\frac{\sin(2\pi x)}{\pi x}
\frac{\sin(2\pi kx)}{\pi x}\\
&=\boxed{\frac{\sin(2\pi x)\sin(2\pi kx)}{\pi^2x^2}}.
\end{aligned}
\]
This function is in $L^1(\mathbb R)$: it is bounded near $0$ and is $O(x^{-2})$ at infinity.
:::

<1>3. Show that the $L^1$ norms of the inverse transforms are unbounded.
::: proof
For $0\le x\le1/4$, concavity of $\sin$ on $[0,\pi/2]$ gives
\[
\sin(2\pi x)\ge4x.
\]
Hence for $k\ge4$,
\[
\begin{aligned}
\|h_k\|_1
&\ge\int_{1/k}^{1/4}|h_k(x)|\,dx\\
&\ge\frac4{\pi^2}
\int_{1/k}^{1/4}\frac{|\sin(2\pi kx)|}{x}\,dx.
\end{aligned}
\]
With $y=kx$ this becomes
\[
\|h_k\|_1
\ge\frac4{\pi^2}
\int_1^{k/4}\frac{|\sin(2\pi y)|}{y}\,dy.
\]
For each integer $j\ge1$,
\[
\int_j^{j+1}|\sin(2\pi y)|\,dy=\frac2\pi,
\]
so
\[
\int_j^{j+1}\frac{|\sin(2\pi y)|}{y}\,dy
\ge\frac2{\pi(j+1)}.
\]
Summing over $1\le j\le\lfloor k/4\rfloor-1$ shows
\[
\|h_k\|_1\longrightarrow\infty.
\]
:::

<1>4. Use the open mapping theorem to rule out surjectivity.
::: proof
The Fourier transform
\[
\mathcal F:L^1(\mathbb R)\to C_0(\mathbb R)
\]
is bounded and injective. Suppose it were onto. Then it would be a bounded linear bijection between Banach spaces, so the bounded inverse theorem would give a constant $C$ such that
\[
\|f\|_1\le C\|\widehat f\|_\infty
\qquad(f\in L^1).
\]

Apply this to $f=h_k$. Since $\widehat{h_k}=g_k$ and $\|g_k\|_\infty=2$,
\[
\|h_k\|_1\le2C
\]
for every $k$, contradicting Step 3. Therefore
\[
\boxed{\mathcal F:L^1(\mathbb R)\to C_0(\mathbb R)\text{ is not onto}.}
\]
:::
:::
