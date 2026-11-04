---
schema: qual/card@1
id: E-SS10.PR-6
kind: problem
title: Eight squares from an Eisenstein series
classification:
  areas:
  - complex-analysis
  topics:
  - Sums of Squares
  - Modular Forms
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 10, §4, exercise 6, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise, including its six parts, the final instruction, and the hint (which supplies the
    Chapter 9 Fourier expansion of $E_4$ and the identity for part (f)). Nothing in the statement was
    changed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    All six parts proved, then used exactly as the exercise directs. Citations, each checked against
    the text: the Fourier expansion of $E_k$ is Chapter 9, Theorem 2.5; the theta transformation is
    Chapter 10, Corollary 1.7; the asymptotic of $\theta(1-1/\tau)$ is Chapter 10, Corollary 1.8; the
    vanishing of $\theta$ on the upper half-plane is Chapter 10, Corollary 1.4; and the criterion
    "holomorphic, invariant under $T_2$ and $S$, bounded, hence constant" is Chapter 10, Theorem 3.4,
    whose proof is not reproduced here. Proved here rather than cited: parts (a)--(f), the arithmetic
    identity for $\sigma_3^*$ in the even case, the modularity of the book's $E_4$ from its defining
    series, and the four properties of $\theta^8$ used at the end. No new formalization was
    undertaken; nothing is deferred.
---

::: {.exercise}
Let $r_8(n)$ count representations of $n$ as a sum of eight squares. Prove $r_8(n)=16\sigma_3^*(n)$, where $\sigma_3^*(n)=\sum_{d\mid n}d^3$ for odd $n$, while for even $n$,
$$
\sigma_3^*(n)=\sum_{d\mid n}(-1)^d d^3.
$$
Define
$$
E_4^*(\tau)=\sum_{\substack{m,n\in\ZZ\\m,n\text{ of opposite parity}}}
\frac1{(n+m\tau)^4},\qquad
E_4(\tau)=\sum_{(m,n)\ne(0,0)}\frac1{(n+m\tau)^4}.
$$

(a) Show that the formula for $r_8(n)$ is equivalent to $\theta(\tau)^8=48\pi^{-4}E_4^*(\tau)$.

(b) Show that $E_4^*(\tau)=E_4(\tau)-2^{-4}E_4((\tau-1)/2)$.

(c) Show that $E_4^*(\tau+2)=E_4^*(\tau)$.

(d) Show that $E_4^*(\tau)=\tau^{-4}E_4^*(-1/\tau)$.

(e) Show that $(48/\pi^4)E_4^*(\tau)\to1$ as $\Im\tau\to\infty$.

(f) Show that $\abs{E_4^*(1-1/\tau)}\asymp\abs{\tau}^4\abs{e^{2\pi i\tau}}$ as $\Im\tau\to\infty$.

Use these properties and the corresponding properties of $\theta^8$ to conclude that $48\pi^{-4}E_4^*/\theta^8$ is identically $1$.
:::

::: {.hint}
For (a), use $E_4(\tau)=2\zeta(4)+(2\pi)^4\sum_{k\geq1}\sigma_3(k)e^{2\pi ik\tau}/3$ and $\zeta(4)=\pi^4/90$. For (f), verify $E_4^*(1-1/\tau)=\tau^4(E_4(\tau)-E_4(2\tau))$.
:::

::: {.solution}

Write $q=e^{\pi i\tau}$ for $\tau$ in the upper half-plane $\HH$, so that $\theta(\tau)=\sum_{n}q^{n^2}$ and $\theta(\tau)^8=\sum_{n\ge0}r_8(n)q^n$, and write $Q=e^{2\pi i\tau}=q^2$, which is the variable of the Eisenstein expansions. Both series defining $E_4$ and $E_4^*$ converge absolutely on $\HH$, because $\abs{n+m\tau}\ge c\max(\abs{m},\abs{n})$ there with $c>0$ depending on $\tau$, so every rearrangement of them below is legitimate.

::: pf

::: {.pf-step #s1}

$E_4^*(\tau)=E_4(\tau)-2^{-4}E_4((\tau-1)/2)$.

::: pf-proof

For $(m,n)\ne(0,0)$ one has
$$
n+m\frac{\tau-1}{2}=\frac{(2n-m)+m\tau}{2}.
$$
The map $(m,n)\mapsto(2n-m,m)$ is a bijection of $\ZZ^2\setminus\{0\}$ onto the set of pairs $(k,l)\ne(0,0)$ with $k\equiv l \pmod 2$, with inverse $(k,l)\mapsto(l,(k+l)/2)$. Hence
$$
E_4\Bigl(\frac{\tau-1}{2}\Bigr)=2^4\sum_{\substack{k\equiv l\!\!\pmod 2\\(k,l)\ne(0,0)}}\frac{1}{(k+l\tau)^4}.
$$
The pairs of equal parity and the pairs of opposite parity partition $\ZZ^2\setminus\{0\}$, and $E_4^*$ is by definition the sum over the opposite-parity pairs. Therefore
$$
2^{-4}E_4\Bigl(\frac{\tau-1}{2}\Bigr)+E_4^*(\tau)=E_4(\tau).
$$

:::

:::

::: {.pf-step #s2}

$E_4^*(\tau+2)=E_4^*(\tau)$.

::: pf-proof

For $(m,n)$ of opposite parity,
$$
n+m(\tau+2)=(n+2m)+m\tau .
$$
Since $2m$ is even, $n+2m$ has the same parity as $n$, so $(m,n+2m)$ is again a pair of opposite parity; and $(m,n)\mapsto(m,n+2m)$ is a bijection of $\ZZ^2$ onto itself. Summing over the opposite-parity pairs gives $E_4^*(\tau+2)=E_4^*(\tau)$.

:::

:::

::: {.pf-step #s3}

$E_4^*(\tau)=\tau^{-4}E_4^*(-1/\tau)$.

::: pf-proof

Replacing $\tau$ by $-1/\tau$ and multiplying numerator and denominator by $\tau^4$,
$$
E_4^*(-1/\tau)=\sum_{\substack{(m,n)\ne(0,0)\\ m,n\text{ opposite parity}}}\frac{\tau^4}{(n\tau-m)^4}
=\tau^4\sum_{\substack{(m,n)\ne(0,0)\\ m,n\text{ opposite parity}}}\frac{1}{(-m)+n\tau}.
$$
The map $(m,n)\mapsto(n,-m)$ is a bijection of $\ZZ^2$ onto itself, and $-m$ has the parity of $m$, so it carries the opposite-parity pairs to the opposite-parity pairs; moreover $(-m)+n\tau=n'+m'\tau$ for $(m',n')=(n,-m)$. Hence
$$
E_4^*(-1/\tau)=\tau^4E_4^*(\tau).
$$

:::

:::

::: {.pf-step #s4}

$E_4$ is a modular form of weight $4$ for $SL_2(\ZZ)$: $E_4(\tau+1)=E_4(\tau)$ and $E_4(-1/\tau)=\tau^4E_4(\tau)$, hence $E_4\bigl(\frac{a\tau+b}{c\tau+d}\bigr)=(c\tau+d)^4E_4(\tau)$ for $\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)\in SL_2(\ZZ)$.

::: pf-proof

The two identities are the arguments of steps [](#s1){.pf-ref} and [](#s3){.pf-ref} with $E_4^*$ replaced by $E_4$: in the first, $n+m(\tau+1)=(n+m)+m\tau$ and $(m,n)\mapsto(m,n+m)$ is a bijection of $\ZZ^2$; in the second the computation is verbatim that of step [](#s3){.pf-ref} without the parity restriction. Since $T:\tau\mapsto\tau+1$ and $S:\tau\mapsto-1/\tau$ generate $SL_2(\ZZ)$, the displayed formula follows by composing the two identities.

:::

:::

::: {.pf-step #s5}

For $\tau\in\HH$,
$$
\frac{48}{\pi^4}E_4^*(\tau)=1+256\sum_{r\ge1}\sigma_3(r)q^{2r}-16\sum_{r\ge1}(-1)^r\sigma_3(r)q^{r}.
$$

::: pf-proof

By Chapter 9, Theorem 2.5 with $k=4$, in which the variable of the expansion is $e^{2\pi i\tau}$,
$$
E_4(w)=2\zeta(4)+\frac{16\pi^4}{3}\sum_{r\ge1}\sigma_3(r)e^{2\pi irw},
\qquad \zeta(4)=\frac{\pi^4}{90},\quad 2\zeta(4)=\frac{\pi^4}{45}.
$$
Apply this at $w=\tau$ and at $w=(\tau-1)/2$, where $e^{2\pi iw}=e^{\pi i(\tau-1)}=-q$:
$$
E_4(\tau)=\frac{\pi^4}{45}+\frac{16\pi^4}{3}\sum_{r\ge1}\sigma_3(r)q^{2r},
\qquad
E_4\Bigl(\frac{\tau-1}{2}\Bigr)=\frac{\pi^4}{45}+\frac{16\pi^4}{3}\sum_{r\ge1}\sigma_3(r)(-q)^{r}.
$$
Substituting these into step [](#s1){.pf-ref} and using $2^{-4}=1/16$,
$$
E_4^*(\tau)=\frac{\pi^4}{45}\Bigl(1-\frac{1}{16}\Bigr)
+\frac{16\pi^4}{3}\sum_{r\ge1}\sigma_3(r)q^{2r}
-\frac{\pi^4}{3}\sum_{r\ge1}(-1)^r\sigma_3(r)q^{r},
$$
and $\frac{\pi^4}{45}\cdot\frac{15}{16}=\frac{\pi^4}{48}$. Multiplying by $48/\pi^4$ gives the displayed identity, since $\frac{48}{\pi^4}\cdot\frac{16\pi^4}{3}=256$ and $\frac{48}{\pi^4}\cdot\frac{\pi^4}{3}=16$.

:::

:::

::: {.pf-step #s6}

For even $n\ge2$,
$$
\sum_{d\mid n}(-1)^d d^3=16\sigma_3(n/2)-\sigma_3(n).
$$

::: pf-proof

Let $n=2m$ with $m=2^{a}m'$, $m'$ odd. The divisors of $n$ that are odd are the divisors of $m'$, and those that are even are $2e$ with $e\mid m$. Hence
$$
\sum_{d\mid n}(-1)^d d^3=-\sigma_3(m')+\sum_{e\mid m}(2e)^3=-\sigma_3(m')+8\sigma_3(m).
$$
Since $\sigma_3$ is multiplicative on coprime factors, $\sigma_3(m)=\frac{8^{a+1}-1}{7}\sigma_3(m')$ and $\sigma_3(n)=\sigma_3(2m)=\frac{8^{a+2}-1}{7}\sigma_3(m')$. Therefore
$$
-\sigma_3(m')+8\sigma_3(m)=\sigma_3(m')\Bigl(-1+\frac{8(8^{a+1}-1)}{7}\Bigr)=\sigma_3(m')\frac{8^{a+2}-15}{7},
$$
and
$$
16\sigma_3(m)-\sigma_3(n)=\sigma_3(m')\frac{16(8^{a+1}-1)-(8^{a+2}-1)}{7}=\sigma_3(m')\frac{8^{a+2}-15}{7},
$$
because $16\cdot 8^{a+1}=2\cdot 8^{a+2}$. The two expressions agree.

:::

:::

::: {.pf-step #s7}

The identity $r_8(n)=16\sigma_3^*(n)$ for all $n\ge1$ is equivalent to $\theta(\tau)^8=48\pi^{-4}E_4^*(\tau)$.

::: pf-proof

By step [](#s5){.pf-ref}, the coefficient of $q^0$ in $48\pi^{-4}E_4^*$ is $1$, and for $n\ge1$ its coefficient $c_n$ is read off as follows. If $n$ is odd, only the second sum contributes, at $r=n$, and
$$
c_n=-16(-1)^n\sigma_3(n)=16\sigma_3(n)=16\sigma_3^*(n),
$$
because $\sigma_3^*(n)=\sigma_3(n)$ for odd $n$. If $n$ is even, the first sum contributes at $r=n/2$ and the second at $r=n$:
$$
c_n=256\sigma_3(n/2)-16\sigma_3(n)=16\bigl(16\sigma_3(n/2)-\sigma_3(n)\bigr)=16\sigma_3^*(n)
$$
by step [](#s6){.pf-ref}. Hence
$$
\frac{48}{\pi^4}E_4^*(\tau)=1+\sum_{n\ge1}16\sigma_3^*(n)q^n .
$$
On the other hand $\theta(\tau)^8=\sum_{n\ge0}r_8(n)q^n$ with $r_8(0)=1$, since $\theta(\tau)=\sum_n q^{n^2}$ and $r_8(n)$ counts the eight-tuples of integers with $\sum_j n_j^2=n$. Two holomorphic functions on $\HH$ with the same Fourier series in $q=e^{\pi i\tau}$ are equal, so the two displayed identities are equivalent.

:::

:::

::: {.pf-step #s8}

$\frac{48}{\pi^4}E_4^*(\tau)\to1$ as $\operatorname{Im}(\tau)\to\infty$.

::: pf-proof

By step [](#s5){.pf-ref},
$$
\Bigl|\frac{48}{\pi^4}E_4^*(\tau)-1\Bigr|\le 256\sum_{r\ge1}\sigma_3(r)\abs{q}^{2r}+16\sum_{r\ge1}\sigma_3(r)\abs{q}^{r}.
$$
Since $\sigma_3(r)\le r\cdot r^3=r^4$ and $\abs{q}=e^{-\pi\operatorname{Im}\tau}<1$, both series are dominated by $\sum_r r^4\abs{q}^{r}$, which is finite and tends to $0$ as $\abs{q}\to0$, that is, as $\operatorname{Im}(\tau)\to\infty$.

:::

:::

::: {.pf-step #s9}

$E_4^*(1-1/\tau)=\tau^4\bigl(E_4(\tau)-E_4(2\tau)\bigr)$, and consequently $\abs{E_4^*(1-1/\tau)}\asymp\abs{\tau}^4\abs{e^{2\pi i\tau}}$ as $\operatorname{Im}(\tau)\to\infty$.

::: pf-proof

By step [](#s1){.pf-ref} at $\sigma=1-1/\tau$, where $(\sigma-1)/2=-1/(2\tau)$,
$$
E_4^*(1-1/\tau)=E_4(1-1/\tau)-2^{-4}E_4(-1/(2\tau)).
$$
Now $1-1/\tau=\frac{\tau-1}{\tau}$ is the image of $\tau$ under $\bigl(\begin{smallmatrix}1&-1\\1&0\end{smallmatrix}\bigr)\in SL_2(\ZZ)$, whose $c\tau+d$ is $\tau$, so step [](#s4){.pf-ref} gives $E_4(1-1/\tau)=\tau^4E_4(\tau)$; and step [](#s4){.pf-ref} at the argument $2\tau$ gives $E_4(-1/(2\tau))=(2\tau)^4E_4(2\tau)=16\tau^4E_4(2\tau)$. Hence
$$
E_4^*(1-1/\tau)=\tau^4E_4(\tau)-2^{-4}\cdot16\tau^4E_4(2\tau)=\tau^4\bigl(E_4(\tau)-E_4(2\tau)\bigr).
$$
By Chapter 9, Theorem 2.5 the constant terms cancel in the difference, and with $Q=e^{2\pi i\tau}$
$$
E_4(\tau)-E_4(2\tau)=\frac{16\pi^4}{3}\sum_{r\ge1}\sigma_3(r)\bigl(Q^{r}-Q^{2r}\bigr)=\frac{16\pi^4}{3}Q\bigl(1+O(Q)\bigr).
$$
Therefore $\abs{E_4^*(1-1/\tau)}=\abs{\tau}^4\frac{16\pi^4}{3}\abs{Q}\bigl(1+O(\abs{Q})\bigr)$, which is the assertion since $\abs{Q}=\abs{e^{2\pi i\tau}}\to0$.

:::

:::

::: {.pf-step #s10}

$\theta^8$ satisfies the same four properties: $\theta(\tau+2)^8=\theta(\tau)^8$, $\theta(-1/\tau)^8=\tau^4\theta(\tau)^8$, $\theta(\tau)^8\to1$ as $\operatorname{Im}(\tau)\to\infty$, and $\abs{\theta(1-1/\tau)^8}\asymp\abs{\tau}^4\abs{e^{2\pi i\tau}}$ as $\operatorname{Im}(\tau)\to\infty$.

::: pf-proof

The first is immediate from $e^{\pi i n^2(\tau+2)}=e^{\pi in^2\tau}e^{2\pi in^2}=e^{\pi in^2\tau}$. The second is Chapter 10, Corollary 1.7, $\theta(-1/\tau)=(\tau/i)^{1/2}\theta(\tau)$, raised to the eighth power, with $(\tau/i)^4=\tau^4/i^4=\tau^4$. For the third, $\theta(\tau)=1+2q+2q^4+\cdots$ with $\abs{q}\to0$, so $\theta(\tau)^8\to1$. For the fourth, Chapter 10, Corollary 1.8 gives $\theta(1-1/\tau)\sim(\tau/i)^{1/2}2e^{\pi i\tau/4}$ as $\operatorname{Im}(\tau)\to\infty$, and raising to the eighth power gives $\theta(1-1/\tau)^8\sim256\,\tau^4e^{2\pi i\tau}$.

:::

:::

::: {.pf-step #s11}

The function $f=(48/\pi^4)E_4^*/\theta^8$ is holomorphic on $\HH$, satisfies $f(\tau+2)=f(\tau)$ and $f(-1/\tau)=f(\tau)$, and is bounded.

::: pf-proof

$\theta$ does not vanish on $\HH$ by Chapter 10, Corollary 1.4, so $f$ is holomorphic. Steps [](#s2){.pf-ref} and [](#s10){.pf-ref} give $f(\tau+2)=f(\tau)$; steps [](#s3){.pf-ref} and [](#s10){.pf-ref} give
$$
f(-1/\tau)=\frac{(48/\pi^4)\tau^4E_4^*(\tau)}{\tau^4\theta(\tau)^8}=f(\tau).
$$

For boundedness, let $\mathcal F=\{\tau\in\HH:\abs{\operatorname{Re}\tau}\le1,\ \abs{\tau}\ge1\}$ and let $\overline{\mathcal F}$ be its closure in $\HH$ together with the two cusps $\pm1$. On $\mathcal F$ the function $f$ is continuous. As $\operatorname{Im}(\tau)\to\infty$ within $\mathcal F$, step [](#s8){.pf-ref} and step [](#s10){.pf-ref} give $f(\tau)\to1$. As $\tau\to1$ within $\mathcal F$, write $\tau=1-1/\tau'$ with $\operatorname{Im}(\tau')\to\infty$; then by step [](#s9){.pf-ref} and step [](#s10){.pf-ref},
$$
f(\tau)=\frac{48}{\pi^4}\cdot\frac{\tau'^4\bigl(\frac{16\pi^4}{3}e^{2\pi i\tau'}+O(e^{4\pi i\tau'})\bigr)}{256\,\tau'^4e^{2\pi i\tau'}(1+o(1))}\longrightarrow\frac{48}{\pi^4}\cdot\frac{16\pi^4}{3\cdot256}=1 .
$$
The case $\tau\to-1$ is the same after $\tau\mapsto\tau+2$. Hence $f$ extends continuously to $\overline{\mathcal F}$ with the value $1$ at the cusps, so $f$ is bounded on $\mathcal F$; and every point of $\HH$ is carried into $\mathcal F$ by the group generated by $T_2$ and $S$ (Chapter 10, Lemma 3.5), under which $f$ is invariant. Hence $f$ is bounded on $\HH$.

:::

:::

::: {.pf-step #s12}

$f\equiv1$, hence $\theta(\tau)^8=48\pi^{-4}E_4^*(\tau)$ and $r_8(n)=16\sigma_3^*(n)$ for all $n\ge1$.

::: pf-proof

By step [](#s11){.pf-ref}, $f$ is holomorphic on $\HH$, invariant under $T_2:\tau\mapsto\tau+2$ and $S:\tau\mapsto-1/\tau$, and bounded. Chapter 10, Theorem 3.4 then gives that $f$ is constant. Its value is the limit at the cusp, which is $1$ by step [](#s8){.pf-ref} and step [](#s10){.pf-ref}. Hence $\theta^8=48\pi^{-4}E_4^*$, and step [](#s7){.pf-ref} converts this identity into $r_8(n)=16\sigma_3^*(n)$ for every $n\ge1$.

:::

:::

:::

:::
