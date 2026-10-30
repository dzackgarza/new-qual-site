---
schema: qual/card@1
id: P-UCLARA18F-04
kind: problem
title: Unique ergodicity of irrational rotations of the circle
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 4. Let $\circlegroup$ be the unit circle in the complex plane $\CC$, and for each $\alpha\in\circlegroup$ define the rotation map $R_\alpha:\circlegroup\to\circlegroup$ by
$$
R_\alpha(z)=\alpha z.
$$
A Borel probability measure $\mu$ on $\circlegroup$ is called $\alpha$-invariant if
$$
\mu(R_\alpha(E))=\mu(E)
$$
for every Borel set $E\subset\circlegroup$.

(a) Let $m$ be Lebesgue measure on $\circlegroup$ (defined, for instance, by identifying $\circlegroup$ with $[0,1)$ through the exponential function). Show that for every $\alpha\in\circlegroup$, $m$ is $\alpha$-invariant.

(b) Prove that if $\alpha$ is not a root of unity, then the set of powers $\{\alpha^n:n\in\ZZ\}$ is dense in $\circlegroup$.

(c) Prove that, if we fix a single $\alpha\in\circlegroup$ which is not a root of unity, then $m$ is the only $\alpha$-invariant Borel probability measure on $\circlegroup$.
:::

::: {.solution}

Write $q(t)=e^{2\pi i t}$, so that $\circlegroup\cong\RR/\ZZ$, and let $m$ be normalized Lebesgue measure under this identification.

::: pf

::: {.pf-step #s1-1}

For every $\alpha\in\circlegroup$, the measure $m$ is $\alpha$-invariant.


::: pf-proof

Write $\alpha=q(a)$ with $0\le a<1$. Under $\circlegroup\cong[0,1)$, the rotation $R_\alpha$ is
$$
\tau_a(t)=t+a\pmod 1.
$$
For a Borel set $E\subseteq[0,1)$, split
$$
E=E_0\sqcup E_1,
\qquad
E_0=E\cap[0,1-a),
\qquad
E_1=E\cap[1-a,1).
$$
Then
$$
\tau_a(E)=(E_0+a)\sqcup(E_1+a-1).
$$
The two pieces are disjoint, and translation invariance of Lebesgue measure on $\RR$ gives
$$
m(\tau_a(E))=m(E_0)+m(E_1)=m(E).
$$
Thus $m(R_\alpha(E))=m(E)$ for every Borel $E\subseteq\circlegroup$.

:::

:::

::: {.pf-step #s1-2}

Let $H\subseteq\circlegroup$ be an infinite subgroup and let $\overline H$ be its closure. Then points of $H\setminus\{1\}$ occur arbitrarily close to $1$.


::: pf-proof

The compact set $\overline H$ contains infinitely many points, so $H$ has an accumulation point $z\in\circlegroup$. Choose pairwise distinct $h_j\in H$ with $h_j\to z$. Then
$$
h_{2j}h_{2j-1}^{-1}\in H\setminus\{1\}
$$
for every $j$, while $h_{2j}h_{2j-1}^{-1}\to zz^{-1}=1$. Hence nonidentity elements of $H$ lie arbitrarily close to $1$.

:::

:::

::: {.pf-step #s1-3}

Every infinite subgroup $H\subseteq\circlegroup$ is dense in $\circlegroup$.


::: pf-proof

Fix $\varepsilon>0$. By step [](#s1-2){.pf-ref}, choose
$$
h=e^{2\pi i\theta}\in H\setminus\{1\}
$$
with $0<\abs{\theta}<\varepsilon$, after choosing the representative $\theta\in(-1/2,1/2]$. Replacing $h$ by $h^{-1}$ if necessary, assume $0<\theta<\varepsilon$.

Let $N=\lfloor1/\theta\rfloor$. The points
$$
0,\theta,2\theta,\ldots,N\theta
$$
partition $[0,1]$ into gaps of length $\theta$, except for the final gap $1-N\theta<\theta$. Therefore the powers
$$
1,h,h^2,\ldots,h^N\in H
$$
form an $\varepsilon$-net in $\circlegroup$. Since $\varepsilon>0$ was arbitrary, $H$ is dense.

:::

:::

::: {.pf-step #s1-4}

If $\alpha$ is not a root of unity, then
$$
\boxed{\{\alpha^n:n\in\ZZ\}\text{ is dense in }\circlegroup}.
$$


::: pf-proof

The cyclic subgroup $H=\{\alpha^n:n\in\ZZ\}$ is finite exactly when $\alpha$ has finite order, i.e. exactly when $\alpha$ is a root of unity. Under the hypothesis it is infinite, so step [](#s1-3){.pf-ref} applies.

:::

:::

::: {.pf-step #s1-5}

If $\mu$ is $\alpha$-invariant, then $\mu$ is invariant under $R_{\alpha^n}$ for every $n\in\ZZ$.


::: pf-proof

Positive powers follow by iteration. For the inverse rotation, if $E$ is Borel and $F=R_{\alpha^{-1}}(E)$, then $R_\alpha(F)=E$, so
$$
\mu(E)=\mu(R_\alpha(F))=\mu(F)=\mu(R_{\alpha^{-1}}(E)).
$$
Iteration gives invariance for all negative powers as well.

:::

:::

::: {.pf-step #s1-6}

Assume $\alpha$ is not a root of unity. If $\mu$ is $\alpha$-invariant, then for every $\beta\in\circlegroup$ and every $f\in C(\circlegroup)$,
$$
\int_{\circlegroup}f(\beta z)\,d\mu(z)
=\int_{\circlegroup}f(z)\,d\mu(z).
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, choose integers $n_j$ with $\alpha^{n_j}\to\beta$. Since $f$ is uniformly continuous on compact $\circlegroup$,
$$
f(\alpha^{n_j}z)\longrightarrow f(\beta z)
$$
uniformly in $z$. Step [](#s1-5){.pf-ref} gives
$$
\int f(\alpha^{n_j}z)\,d\mu(z)=\int f(z)\,d\mu(z)
$$
for every $j$. Passing to the limit under the integral, justified by uniform convergence, proves the claim.

:::

:::

::: {.pf-step #s1-7}

Under the same hypotheses, for every $f\in C(\circlegroup)$,
$$
\int_{\circlegroup}f\,d\mu=\int_{\circlegroup}f\,dm.
$$


::: pf-proof

By step [](#s1-6){.pf-ref}, the inner integral below is independent of $\beta$. Hence Fubini's theorem and step [](#s1-1){.pf-ref} give
$$
\begin{aligned}
\int_{\circlegroup}f(z)\,d\mu(z)
&=\int_{\circlegroup}\int_{\circlegroup}f(\beta z)\,d\mu(z)\,dm(\beta)\\
&=\int_{\circlegroup}\int_{\circlegroup}f(\beta z)\,dm(\beta)\,d\mu(z)\\
&=\int_{\circlegroup}\left(\int_{\circlegroup}f(\beta)\,dm(\beta)\right)d\mu(z)\\
&=\int_{\circlegroup}f\,dm.
\end{aligned}
$$
In the third line, multiplication by the fixed $z\in\circlegroup$ is a rotation, so it preserves $m$ by step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

If $\alpha$ is not a root of unity, then $\boxed{m\text{ is the unique }\alpha\text{-invariant Borel probability measure}}$.


::: pf-proof

Existence is step [](#s1-1){.pf-ref}. If $\mu$ is any other $\alpha$-invariant Borel probability measure, step [](#s1-7){.pf-ref} shows that $\mu$ and $m$ have the same integral against every real-valued continuous function on compact $\circlegroup$. By uniqueness in the Riesz representation theorem, $\mu=m$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-4){.pf-ref}, and [](#s1-8){.pf-ref} prove parts (a), (b), and (c), respectively.

:::

:::

:::
