---
schema: qual/card@1
id: P-UCLARA15S-03
kind: problem
title: Refined weak-type bound for the Hardy--Littlewood maximal function
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2015, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $f\in L^1_{\mathrm{loc}}(\RR^n)$ and let
$$
Mf(x)=\sup_{r>0}\frac1{m(B(r,x))}\int_{B(r,x)}\abs{f(y)}\,dy
$$
be the Hardy--Littlewood maximal function.

(a) Show that
$$
m(\{x:Mf(x)>s\})\le\frac{C_n}{s}\int_{\abs{f(x)}>s/2}\abs{f(x)}\,dx,\qquad s>0,
$$
where $C_n$ depends only on $n$.
The Hardy--Littlewood maximal theorem may be used.

(b) Prove that if $\phi\in C^1(\RR)$, $\phi(0)=0$, and $\phi'>0$, then
$$
\int \phi(Mf(x))\,dx\le C_n\int \abs{f(x)}\left(\int_{0<t<2\abs{f(x)}}\frac{\phi'(t)}t\,dt\right)dx.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Fix $s>0$ and define
$$
\widetilde f_s(x)
\coloneqq
f(x)\mathbf 1_{\{\abs{f(x)}>s/2\}}.
$$
Then
$$
\{x:Mf(x)>s\}
\subseteq
\{x:M\widetilde f_s(x)>s/2\}.
$$


::: pf-proof

Suppose $Mf(x)>s$. Then there is a ball $B$ centered at $x$ such that
$$
\frac1{m(B)}
\int_B\abs{f(y)}\,dy
>s.
$$
Split the integral according to whether $\abs{f}\le s/2$ or $\abs{f}>s/2$:
$$
\begin{aligned}
s\,m(B)
&<
\int_{B\cap\{\abs{f}\le s/2\}}\abs{f}
+
\int_{B\cap\{\abs{f}>s/2\}}\abs{f}\\
&\le
\frac{s}{2}m(B)
+
\int_B\abs{\widetilde f_s}.
\end{aligned}
$$
Hence
$$
\frac1{m(B)}
\int_B\abs{\widetilde f_s}
>
\frac{s}{2}.
$$
Taking the supremum over balls centered at $x$ gives
$$
M\widetilde f_s(x)>s/2.
$$

:::

:::

::: {.pf-step #s1-2}

There is a dimensional constant $C_n$ such that
$$
\boxed{
m(\{x:Mf(x)>s\})
\le
\frac{C_n}{s}
\int_{\abs{f(x)}>s/2}\abs{f(x)}\,dx
}.
$$


::: pf-proof

If
$$
\int_{\abs{f}>s/2}\abs{f}=\infty,
$$
the asserted inequality is automatic. Otherwise
$$
\widetilde f_s\in L^1(\RR^n).
$$
By step [](#s1-1){.pf-ref} and the weak-$(1,1)$ Hardy--Littlewood maximal inequality,
$$
\begin{aligned}
m(\{Mf>s\})
&\le
m(\{M\widetilde f_s>s/2\})\\
&\le
\frac{C_n}{s}
\norm{\widetilde f_s}_1\\
&=
\frac{C_n}{s}
\int_{\abs{f}>s/2}\abs{f}.
\end{aligned}
$$
Absorbing the harmless factor $2$ from the threshold $s/2$ into $C_n$ gives the displayed estimate.

:::

:::

::: {.pf-step #s1-3}

For every nonnegative measurable function $H$,
$$
\int_{\RR^n}\phi(H(x))\,dx
=
\int_0^\infty
\phi'(t)
m(\{x:H(x)>t\})\,dt,
$$
with both sides interpreted in $[0,\infty]$.


::: pf-proof

Since $\phi(0)=0$ and $\phi'>0$,
$$
\phi(H(x))
=
\int_0^{H(x)}\phi'(t)\,dt
=
\int_0^\infty
\phi'(t)
\mathbf 1_{\{t<H(x)\}}\,dt.
$$
The integrand is nonnegative, so Tonelli's theorem gives
$$
\begin{aligned}
\int_{\RR^n}\phi(H(x))\,dx
&=
\int_0^\infty
\phi'(t)
\left(
\int_{\RR^n}
\mathbf 1_{\{H(x)>t\}}\,dx
\right)dt\\
&=
\int_0^\infty
\phi'(t)
m(\{H>t\})\,dt.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

Applying step [](#s1-3){.pf-ref} with $H=Mf$ and then step [](#s1-2){.pf-ref} gives
$$
\int_{\RR^n}\phi(Mf(x))\,dx
\le
C_n
\int_0^\infty
\frac{\phi'(t)}{t}
\left(
\int_{\abs{f(x)}>t/2}\abs{f(x)}\,dx
\right)dt.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} gives
$$
\int\phi(Mf)
=
\int_0^\infty
\phi'(t)m(\{Mf>t\})\,dt.
$$
Substitute the estimate from step [](#s1-2){.pf-ref} for each $t>0$. Since every quantity is nonnegative, the inequality remains valid even when one or both sides are infinite.

:::

:::

::: {.pf-step #s1-5}

The right-hand side in step [](#s1-4){.pf-ref} equals
$$
C_n
\int_{\RR^n}
\abs{f(x)}
\left(
\int_{0<t<2\abs{f(x)}}
\frac{\phi'(t)}{t}\,dt
\right)dx.
$$


::: pf-proof

The integrand is nonnegative, so Tonelli's theorem permits reversing the order of integration:
$$
\begin{aligned}
&\int_0^\infty
\frac{\phi'(t)}{t}
\left(
\int_{\abs{f(x)}>t/2}\abs{f(x)}\,dx
\right)dt\\
&\qquad=
\int_{\RR^n}
\abs{f(x)}
\left(
\int_{\{t>0:t<2\abs{f(x)}\}}
\frac{\phi'(t)}{t}\,dt
\right)dx.
\end{aligned}
$$
This is the claimed expression.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\int \phi(Mf(x))\,dx
\le
C_n\int \abs{f(x)}
\left(
\int_{0<t<2\abs{f(x)}}
\frac{\phi'(t)}t\,dt
\right)dx
}.
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (a), and step [](#s1-6){.pf-ref} proves part (b).

:::

:::

:::
