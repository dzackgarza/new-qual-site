---
schema: qual/card@1
id: E-SS9.EX-8
kind: problem
title: "SS 9.8: Decay of the Eisenstein series E4 toward the cusp"
classification:
  areas:
  - complex-analysis
  topics: ['Elliptic Functions', 'Weierstrass P', 'Lattices']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
8. Let

$$
E _ {4} (\tau) = \sum_ {(n, m) \neq (0, 0)} \frac {1}{(n + m \tau) ^ {4}}
$$

be the Eisenstein series of order 4.

(a) Show that $E _ { 4 } ( \tau ) \to \pi ^ { 4 } / 4 5 { \mathrm { ~ a s ~ I m } } ( \tau ) \to \infty$

(b) More precisely,

$$
\left| E _ {4} (\tau) - \frac {\pi^ {4}}{4 5} \right| \leq c e ^ {- 2 \pi t} \quad \text { if } \tau = x + i t \text { and } t \geq 1.
$$

(c) Deduce that

$$
\left| E _ {4} (\tau) - \tau^ {- 4} \frac {\pi^ {4}}{4 5} \right| \leq c t ^ {- 4} e ^ {- 2 \pi / t} \quad \text { if } \tau = i t \text { and } 0 <   t \leq 1.
$$
:::

::: solution
Separate the terms with \(m=0\):
\[
E_4(\tau)=2\zeta(4)+\sum_{m\ne0}\sum_{n\in\mathbb Z}(n+m\tau)^{-4}.
\]
For \(\Im w>0\), Exercise 7 of Chapter 4 gives
\[
\sum_{n\in\mathbb Z}(n+w)^{-4}
=\frac{8\pi^4}{3}\sum_{r=1}^\infty r^3e^{2\pi irw}.
\tag{1}
\]
The contributions of \(m\) and \(-m\) are equal (replace \(n\) by \(-n\)). Hence, for \(\tau=x+it\),
\[
E_4(\tau)=\frac{\pi^4}{45}
+\frac{16\pi^4}{3}\sum_{m=1}^\infty\sum_{r=1}^\infty r^3e^{2\pi irm\tau},
\tag{2}
\]
because \(2\zeta(4)=\pi^4/45\).

If \(t\ge1\), taking absolute values in (2) gives
\[
\left|E_4(\tau)-\frac{\pi^4}{45}\right|
\le \frac{16\pi^4}{3}\sum_{m,r\ge1}r^3e^{-2\pi rmt}.
\]
Since \(e^{-2\pi rmt}\le e^{-2\pi t}e^{-2\pi(rm-1)}\) for \(t\ge1\), the remaining double sum is finite and independent of \(t\). Thus
\[
\left|E_4(\tau)-\frac{\pi^4}{45}\right|\le Ce^{-2\pi t}.
\]
Part (a) follows immediately.

For part (c), reindexing the lattice gives the modular transformation
\[
E_4(-1/\tau)
=\sum_{(n,m)\ne(0,0)}(n-m/\tau)^{-4}
=\tau^4E_4(\tau).
\tag{3}
\]
Take \(\tau=it\), \(0<t\le1\). Since \(-1/(it)=i/t\), equation (3) yields
\[
E_4(it)=t^{-4}E_4(i/t).
\]
Applying part (b) at height \(1/t\ge1\),
\[
\left|E_4(it)-t^{-4}\frac{\pi^4}{45}\right|
=t^{-4}\left|E_4(i/t)-\frac{\pi^4}{45}\right|
\le Ct^{-4}e^{-2\pi/t},
\]
as required.
:::
