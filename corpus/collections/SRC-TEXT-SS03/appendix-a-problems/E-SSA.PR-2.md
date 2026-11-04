---
schema: qual/card@1
id: E-SSA.PR-2
kind: problem
title: Stirling's formula with an asymptotic expansion in powers of $s^{-1}$
classification:
  areas:
  - complex-analysis
  topics:
  - Asymptotics
  - Gamma Function
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement transcribed from Stein--Shakarchi, *Complex Analysis*, Appendix A, §5, problem 2,
    read from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (PDF pages 359--363, printed
    pages 341--343). This card did not exist before: the collection had no appendix directory at all,
    and a completeness audit against the book found Appendix A's whole Problems section, items 1--5,
    missing. The transcription was taken from the OCR text layer and cleaned of OCR errors; the
    printed wording, hypotheses and bracketed hints are preserved.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Solution installed: the expansion is obtained from the exact substitution Phi = v^2/2 near x = 1, with A(v) = v/(x(v)-1) giving the coefficients a_j = alpha_{2j}(2j-1)!! and a_1 = 1/12, a Gaussian cut-off Watson lemma for the remainder, and the tails estimated by the book's iteration for e^{-s Phi}. The stated range Re s >= 1/2 is extended to Re s >= 0 through Gamma(s+1) = s Gamma(s).
---

::: {.exercise}
The following is a more precise version of Stirling's formula. There are real constants $a_1=1/12$, $a_2,\dots,a_n,\dots$, so that for every $N>0$
$$
\Gamma(s)=e^{s\log s}e^{-s}\frac{\sqrt{2\pi}}{s^{1/2}}\Bigl(1+\sum_{j=1}^{N}a_js^{-j}+O(s^{-N})\Bigr)\qquad\text{when } s\in S_\delta .
$$
This can be proved by using the results of Problem 1 in place of Proposition 1.3.
:::

::: {.solution}
We write $\log$ for the principal branch, $s^{\alpha}$ for the power defined by it (so that $s^{1/2}$ and $s^{-j}$ are the principal powers), $\delta>0$ and $S_\delta=\{s:\abs{\arg s}\le\pi-\delta\}$ as in the text (printed p. 326), and $F$ for the normalized gamma function
$$
F(s)=\sqrt{\frac{s}{2\pi}}\,\Gamma(s)\,e^{-s\log s+s},
$$
which is meromorphic on $\CC\setminus(-\infty,0]$. Two functions attached to the exact substitution $x=1+u$ are used throughout: $\Phi(u)=u-\log(1+u)$, so that $x-1-\log x=\Phi(x-1)$, and
$$
h(t)=\begin{cases}\dfrac{2\bigl(t-\log(1+t)\bigr)}{t^{2}}, & t>-1,\ t\neq0,\\[2mm] 1,&t=0,\end{cases}
\qquad v(t)=t\sqrt{h(t)},\qquad t=x-1,
$$
where $\sqrt{h}$ is the square root with $\sqrt{h(0)}=1$. By step [](#quadratic){.pf-ref} below, $h$ is holomorphic near $t=0$ with $h(0)=1$, and $v$ is a biholomorphism of a neighbourhood of $0$ onto a neighbourhood of $0$, so the inverse $x(v)=1+t(v)$ is holomorphic near $v=0$. Set
$$
A(v)=\frac{x'(v)}{x(v)},\qquad A(v)=\sum_{n\ge0}\alpha_n v^n\ \text{ near } v=0,\qquad a_j:=\alpha_{2j}\,(2j-1)!!\quad(j\ge0),
$$
with $(2j-1)!!=1\cdot3\cdots(2j-1)$ and $0!!:=1$; finally $\Psi_N(u)=\sum_{j=0}^{N}a_ju^{j}$ (so $\Psi_N$ is a polynomial with $\Psi_N(0)=1$). The proof below produces the constants $a_j$ and shows that they are real and that $a_1=1/12$.

::: pf

::: {.pf-step #integral}
For $\Re(s)>0$,
$$
\Gamma(s)=e^{s\log s-s}\int_0^\infty e^{-s\Phi(x)}\,\frac{dx}{x},
\qquad \Phi(x)=x-1-\log x .
$$

::: pf-proof
For $\Re(s)>0$ substitute $x=st$ in $\Gamma(s)=\int_0^\infty e^{-x}x^{s-1}dx$; this is the computation in the proof of Theorem 2.3, printed p. 326. It gives
$$
\Gamma(s)=s^{s}\int_0^\infty e^{-st}t^{s-1}dt=e^{s\log s-s}\int_0^\infty e^{-s(t-1-\log t)}\,\frac{dt}{t},
$$
using $(st)^{s-1}=s^{s-1}t^{s-1}$, $s^{s}s^{-1}=s^{s-1}$ and $t^{s-1}e^{-st}=e^{-s(t-1-\log t)}e^{-\log t}$. Absolute convergence holds because $\Re(s)>0$ and $t-1-\log t\ge0$ with $t-1-\log t\sim t$ as $t\to\infty$ and $t-1-\log t\sim-\log t$ as $t\to0$.

:::

:::

::: {.pf-step #quadratic}
$\Phi(1+t)=2^{-1}t^{2}h(t)$, $v'(0)=1$, $\Phi(x(v))=v^{2}/2$ for $v$ near $0$, and
$$
\frac{dx}{x}=A(v)\,dv,\qquad A(v)=\frac{v}{x(v)-1},\qquad A(0)=1 .
$$

::: pf-proof
Since $t-\log(1+t)=\int_0^t\frac{\sigma}{1+\sigma}d\sigma=t^{2}\int_0^1\frac{\theta\,d\theta}{1+\theta t}$, the function $h=2\int_0^1\frac{\theta\,d\theta}{1+\theta t}$ is holomorphic for $t\notin(-\infty,-1]$, with $h(0)=2\int_0^1\theta\,d\theta=1$; in particular $h$ is holomorphic and nonvanishing on the disc $\abs{t}<1$, so it has a holomorphic square root $\sqrt h$ there with $\sqrt{h(0)}=1$. Hence $v(t)=t\sqrt{h(t)}$ is holomorphic near $t=0$ with $v'(0)=\sqrt{h(0)}=1$, so by the inverse function theorem $v$ has a holomorphic inverse $t(v)$ near $v=0$ with $t(0)=0$, $t'(0)=1$, and $x(v)=1+t(v)$. Since $v(t)^{2}=t^{2}h(t)=2\Phi(1+t)$, we get $\Phi(x(v))=v^{2}/2$. Differentiating this identity in $v$ gives $2v=2\Phi'(x)x'(v)$ with $\Phi'(x)=1-\frac1x=\frac{x-1}{x}$, hence
$$
A(v)=\frac{x'(v)}{x(v)}=\frac{v}{\Phi'(x(v))\,x(v)}=\frac{v}{x(v)-1},
$$
and $x(v)-1=t(v)=v+O(v^{2})$, so $A(v)=v/(v+O(v^{2}))=1+O(v)$ is holomorphic at $0$ with $A(0)=1$. Finally $\frac{dx}{x}=\frac{x'(v)}{x(v)}dv=A(v)dv$.

:::

:::

::: {.pf-step #coefficients}
$\alpha_1=-1/3$, $\alpha_2=1/12$, all $\alpha_n\in\RR$, and consequently $a_1=1/12$.

::: pf-proof
From $-\log(1+t)=\sum_{m\ge1}(-1)^{m}t^{m}/m$ we get $2\bigl(t-\log(1+t)\bigr)/t^{2}=1-\frac{2t}{3}+\frac{t^{2}}{2}+O(t^{3})$. Using $\sqrt{1+w}=1+\frac w2-\frac{w^{2}}{8}+O(w^{3})$ with $w=-\frac{2t}{3}+\frac{t^{2}}{2}$,
$$
\sqrt{h(t)}=1-\frac{t}{3}+\Bigl(\frac14-\frac18\cdot\frac49\Bigr)t^{2}+O(t^{3})=1-\frac{t}{3}+\frac{7t^{2}}{36}+O(t^{3}),
$$
so $v=t\sqrt{h(t)}=t-\frac{t^{2}}{3}+\frac{7t^{3}}{36}+O(t^{4})$. Writing $t(v)=v+\alpha v^{2}+\beta v^{3}+O(v^{4})$ and substituting,
$$
v=t(v)-\frac{t(v)^{2}}{3}+\frac{7t(v)^{3}}{36}+O(t(v)^{4})
=v+\Bigl(\alpha-\frac13\Bigr)v^{2}+\Bigl(\beta-\frac{2\alpha}{3}+\frac{7}{36}\Bigr)v^{3}+O(v^{4}),
$$
so $\alpha=1/3$ and $\beta=\frac{2}{9}-\frac{7}{36}=\frac{1}{36}$. Then
$$
A(v)=\frac{v}{t(v)}=\frac{1}{1+\frac v3+\frac{v^{2}}{36}+O(v^{3})}=1-\frac v3+\Bigl(\frac19-\frac1{36}\Bigr)v^{2}+O(v^{3})=1-\frac v3+\frac{v^{2}}{12}+O(v^{3}),
$$
that is $\alpha_1=-\frac13$ and $\alpha_2=\frac1{12}$. Since $h$ and $\sqrt{h}$ and $v$ and $t$ have real Taylor coefficients at $0$ (as $h$ is real on $(-1,1)$), so does $A$, hence $\alpha_n\in\RR$. Finally $a_1=\alpha_2\cdot1!!=\frac{1}{12}$.

:::

:::

::: {.pf-step #moments}
For $\Re(\lambda)>0$ and $k\ge0$,
$$
\int_{\RR}e^{-\lambda v^{2}/2}v^{2k}\,dv=(2k-1)!!\,\sqrt{2\pi}\,\lambda^{-k-1/2},
\qquad
\int_{\RR}e^{-\lambda v^{2}/2}v^{2k+1}\,dv=0 .
$$

::: pf-proof
The odd integral vanishes because the integrand is odd and integrable. For the even one, $G(\lambda):=\int_{\RR}e^{-\lambda v^{2}/2}dv=\sqrt{2\pi}\,\lambda^{-1/2}$ (the Gaussian integral, by the change of variables $v=u\sqrt{2}$ and $\int_{\RR}e^{-u^{2}}du=\sqrt\pi$). Both sides are holomorphic in $\lambda$ on $\Re(\lambda)>0$, and differentiating $k$ times under the integral sign is legitimate there (dominated convergence on compact subsets, since $|v^{2k}e^{-\lambda v^{2}/2}|\le C_{k,\lambda_0}e^{-\lambda_0 v^{2}/4}$ for $\Re\lambda\ge\lambda_0$). As $\partial_\lambda^{k}e^{-\lambda v^{2}/2}=(-1)^{k}2^{-k}v^{2k}e^{-\lambda v^{2}/2}$ and $\partial_\lambda^{k}\bigl(\sqrt{2\pi}\lambda^{-1/2}\bigr)=(-1)^{k}2^{-k}(2k-1)!!\sqrt{2\pi}\lambda^{-k-1/2}$, the formula follows.

:::

:::

::: {.pf-step #watson}
Let $\rho>0$, let $B$ be holomorphic on $\abs{v}<2\rho$ with $B=\sum_n\beta_nv^n$ there, and let $\chi\in C_c^\infty(-2\rho,2\rho)$ satisfy $\chi\equiv1$ on $[-\rho,\rho]$. Then for every $\sigma_0>0$ and every $K\ge0$,
$$
\int_{\RR}e^{-sv^{2}/2}B(v)\chi(v)\,dv
=\sum_{k=0}^{K}\beta_{2k}(2k-1)!!\sqrt{2\pi}\,s^{-k-1/2}+O\bigl(\abs{s}^{-K-1}\bigr),
$$
the constant in $O$ depending only on $\rho,\sigma_0,K,B$ and $\chi$, uniformly for $\Re(s)\ge\sigma_0$.

::: pf-proof
Let $P(v)=\sum_{n=0}^{2K+1}\beta_nv^n$ and $R=B\chi-P$. Then $R\in C_c^\infty(\RR)$, $\operatorname{supp}R\subset[-2\rho,2\rho]$, and $R$ vanishes at $v=0$ together with its derivatives of order $\le 2K+1$, because $\chi\equiv1$ on $[-\rho,\rho]$ and $B-P$ vanishes to order $2K+2$ at $0$ there.
By step [](#moments){.pf-ref} applied with $\lambda=s$ (legitimate since $\Re(s)\ge\sigma_0>0$),
$$
\int_{\RR}e^{-sv^{2}/2}P(v)\,dv=\sum_{k=0}^{K}\beta_{2k}\int_{\RR}e^{-sv^{2}/2}v^{2k}\,dv=\sum_{k=0}^{K}\beta_{2k}(2k-1)!!\sqrt{2\pi}s^{-k-1/2},
$$
the odd powers contributing zero. It remains to estimate $\int_{\RR}e^{-sv^{2}/2}R\,dv$.

Since $e^{-sv^{2}/2}=-\frac{1}{sv}\frac{d}{dv}\bigl(e^{-sv^{2}/2}\bigr)$, integration by parts gives, for every $C^{1}$ function $g$ whose support is compact and which vanishes at $0$,
$$
\int_{\RR}e^{-sv^{2}/2}g(v)\,dv=\frac1s\int_{\RR}e^{-sv^{2}/2}\frac{d}{dv}\Bigl(\frac{g}{v}\Bigr)dv :
$$
the boundary terms vanish at $\pm\infty$ because $g$ has compact support, and $g/v$ is $C^{1}$ near $0$ because $g(0)=0$. Put $Dg=(g/v)'$. If $g$ is $C^\infty$ with compact support and vanishes at $0$ to order $q$, then $g/v$ vanishes to order $q-1$ and $Dg$ to order $q-2$, so the formula may be applied again as long as $q-2\ge1$, i.e. as long as $q\ge3$. Applying it $K+1$ times to $g=R$, which is $C^\infty$ with compact support and vanishes at $0$ to order $q=2K+2\ge 2(K+1)$ (so that $q-2m\ge2$ for $m\le K$), we get
$$
\Bigl|\int_{\RR}e^{-sv^{2}/2}R\,dv\Bigr|\le\abs{s}^{-K-1}\int_{\RR}\abs{D^{K+1}R(v)}\,dv,
$$
since $\abs{e^{-sv^{2}/2}}=e^{-\Re(s)v^{2}/2}\le1$ and $D^{K+1}R$ is again $C^\infty$ with compact support.

:::

:::

::: {.pf-step #local}
Let $\rho>0$ be so small that $A$ is holomorphic on $\abs{v}<2\rho$, and let $\eta\in C_c^\infty\bigl((1/2,2)\bigr)$ satisfy
$$
\eta\equiv1\ \text{ on }\ x\bigl([-\rho,\rho]\bigr),\qquad \operatorname{supp}\eta\subset x\bigl((-2\rho,2\rho)\bigr),
$$
which is possible because $x((-2\rho,2\rho))$ is an open neighbourhood of $1=x(0)$ contained in $(1/2,2)$. Then for every integer $N\ge1$, uniformly for $\Re(s)\ge1/2$ and $\abs{s}\ge2$,
$$
\int_0^\infty e^{-s\Phi(x)}\,\eta(x)\,\frac{dx}{x}
=\sum_{k=0}^{N}\alpha_{2k}(2k-1)!!\sqrt{2\pi}\,s^{-k-1/2}+O\bigl(\abs{s}^{-N-1/2}\bigr).
$$

::: pf-proof
Let $\tilde\chi=\eta\circ x$. Then $\tilde\chi\in C_c^\infty\bigl((-2\rho,2\rho)\bigr)$, $\tilde\chi\equiv1$ on $[-\rho,\rho]$, and by steps [](#quadratic){.pf-ref} and [](#integral){.pf-ref} the substitution $x=x(v)$ gives
$$
\int_0^\infty e^{-s\Phi(x)}\eta(x)\frac{dx}{x}
=\int_{\RR}e^{-sv^{2}/2}A(v)\tilde\chi(v)\,dv :
$$
the substitution is a bijection of the interval $x^{-1}(\operatorname{supp}\eta)\subset(-2\rho,2\rho)$ onto $\operatorname{supp}\eta$, and there $\eta(x(v))=\tilde\chi(v)$, while $A(v)\tilde\chi(v)$ is $C^\infty$ with compact support. Step [](#watson){.pf-ref} with $B=A$ (holomorphic on $\abs{v}<2\rho$, Taylor coefficients $\alpha_n$), $\chi=\tilde\chi$ and $K=N$ therefore gives the expansion with remainder $O(\abs{s}^{-N-1})$, which is in particular $O(\abs{s}^{-N-1/2})$.

:::

:::

::: {.pf-step #tails}
With $\eta$ as in step [](#local){.pf-ref}, for every integer $M\ge1$,
$$
\int_0^\infty e^{-s\Phi(x)}\bigl(1-\eta(x)\bigr)\frac{dx}{x}=O\bigl(\abs{s}^{-M}\bigr),
$$
uniformly for $\Re(s)\ge1/2$.

::: pf-proof
Put $\psi(x)=\bigl(1-\eta(x)\bigr)/x$ and $\Phi'(x)=1-\frac1x=\frac{x-1}{x}$, so that $\psi/\Phi'=\bigl(1-\eta(x)\bigr)/(x-1)$. The function $\psi/\Phi'$ lies in $C^\infty\bigl((0,\infty)\bigr)$: $\eta$ is smooth and compactly supported in $(1/2,2)$, $\eta\equiv1$ near $1$ (so $1-\eta$ vanishes identically near $x=1$, where the denominator $x-1$ vanishes), and $\psi/\Phi'=1/(x-1)$ for $x\le1/2$ and for $x\ge2$. Define $D_\Phi f=(f/\Phi')'$.

Since $e^{-s\Phi(x)}=-\frac1s\frac{d}{dx}\bigl(e^{-s\Phi(x)}\bigr)\frac{1}{\Phi'(x)}$ wherever $\eta\neq1$, integration by parts gives, for every $f\in C^{0}\bigl((0,\infty)\bigr)$ which vanishes identically near $x=1$ and for which $f/\Phi'\in C^{1}\bigl((0,\infty)\bigr)$,
$$
\int_0^\infty e^{-s\Phi(x)}f(x)\,dx=-\frac1s\Bigl[e^{-s\Phi(x)}\frac{f(x)}{\Phi'(x)}\Bigr]_0^\infty+\frac1s\int_0^\infty e^{-s\Phi(x)}D_\Phi f(x)\,dx .
$$
For $f=\psi$ the boundary terms vanish: at $x=0$ we have $\abs{e^{-s\Phi(x)}}=e^{-\Re(s)\Phi(x)}\to0$ because $\Phi(x)\to+\infty$ as $x\to0+$ and $\Re(s)\ge1/2$; at $x=\infty$ they vanish because $\Phi(x)\to\infty$ and $f/\Phi'=1/(x-1)$ is bounded there; and no boundary term occurs at $x=1$, where $f$ vanishes identically. Iterating $M$ times (each $D_\Phi^{k}\psi$ is again smooth and, for $x\ge2$, equals a function that is $O(x^{-k-1})$; for $x\le1/2$ it stays bounded, since $D_\Phi$ there acts on smooth functions of $x/(x-1)$) gives
$$
\int_0^\infty e^{-s\Phi(x)}\psi(x)\,dx=(-1)^{M}s^{-M}\int_0^\infty e^{-s\Phi(x)}D_\Phi^{M}\psi(x)\,dx,
$$
and $\int_0^\infty\abs{D_\Phi^{M}\psi}<\infty$, while $\abs{e^{-s\Phi(x)}}=e^{-\Re(s)\Phi(x)}\le1$. This proves the claim.

:::

:::

::: {.pf-step #right}
For every integer $N\ge1$ there are real constants $a_1,\dots,a_N$, given by step [](#coefficients){.pf-ref}, such that uniformly for $\Re(s)\ge1/2$ and $\abs{s}\ge2$,
$$
\Gamma(s)=e^{s\log s}e^{-s}\frac{\sqrt{2\pi}}{s^{1/2}}\Bigl(1+\sum_{j=1}^{N}a_js^{-j}+O\bigl(s^{-N}\bigr)\Bigr).
$$

::: pf-proof
Write $1=\eta+(1-\eta)$ with $\eta$ as in step [](#local){.pf-ref}; by step [](#integral){.pf-ref} the integral $\int_0^\infty e^{-s\Phi(x)}dx/x$ is the sum of the two integrals estimated in steps [](#local){.pf-ref} and [](#tails){.pf-ref}. Hence, for $\Re(s)\ge1/2$ and $\abs{s}\ge2$,
$$
\Gamma(s)=e^{s\log s-s}\Bigl(\sum_{k=0}^{N+1}\alpha_{2k}(2k-1)!!\sqrt{2\pi}s^{-k-1/2}+O\bigl(\abs{s}^{-N-3/2}\bigr)\Bigr).
$$
Multiplying by $e^{-s\log s+s}s^{1/2}(2\pi)^{-1/2}$ gives $\Gamma(s)=e^{s\log s-s}\sqrt{2\pi}s^{-1/2}\bigl(\sum_{k=0}^{N+1}a_ks^{-k}+O(\abs{s}^{-N-1})\bigr)$ with $a_k=\alpha_{2k}(2k-1)!!$; the constants are real and $a_1=1/12$ by step [](#coefficients){.pf-ref}.

:::

:::

::: {.pf-step #recurrence}
The conclusion of step [](#right){.pf-ref} holds uniformly for $\Re(s)\ge0$, $\abs{s}\ge4$, with the same constants $a_j$.

::: pf-proof
By Lemma 1.2 of Chapter 6 (printed p. 161), $\Gamma(s+1)=s\Gamma(s)$; substituting the definition of $F$ gives, for $\abs{s}>1$ and $s\neq0$,
$$
\frac{F(s)}{F(s+1)}
=\frac{\Gamma(s)}{\Gamma(s+1)}\cdot\frac{s^{1/2}}{(s+1)^{1/2}}\cdot e^{-s\log s+s+(s+1)\log(s+1)-(s+1)}
=e^{(s+1)\log(1+1/s)-1}\Bigl(1+\frac1s\Bigr)^{-1/2},
$$
as one checks by writing $(s+1)\log(s+1)=s\log s+\log s+(s+1)\log(1+1/s)$. The factor $E(s)=e^{(s+1)\log(1+1/s)-1}(1+1/s)^{-1/2}$ is holomorphic in $\abs{s}>1$, and $\abs{E(s)}\le C$ there, since $(s+1)\log(1+1/s)=1+O(1/s)$.

Now let $\Re(s)\ge0$ with $\abs{s}\ge4$. Then $\Re(s+1)\ge1\ge1/2$ and $\abs{s+1}\ge\abs{s}-1\ge2$, so step [](#right){.pf-ref} applies at $s+1$, and the scalars $1/(s+1)=s^{-1}(1+1/s)^{-1}$ furnish, for $\abs{s}\ge2$, holomorphic functions of $w=1/s$ on $\abs{w}\le1/2$; hence
$$
F(s)=E(s)\Bigl(\sum_{j=0}^{N}a_j(s+1)^{-j}+O\bigl(\abs{s}^{-N-1}\bigr)\Bigr)
=\sum_{j=0}^{N}b_js^{-j}+O\bigl(\abs{s}^{-N-1}\bigr)
$$
for some real constants $b_0,\dots,b_N$, by expanding the product in powers of $w=1/s$ and truncating (the remainders are dominated by a constant times $\abs{w}^{N+1}$, as $\abs{w}\le1/2$). Both this expansion and the one of step [](#right){.pf-ref} hold on the overlap $\{\Re(s)\ge1/2,\abs{s}\ge4\}$; subtracting them and multiplying by $s^{j}$ yields $b_j-a_j=O(\abs{s}^{-N+j})$, so $b_j=a_j$ for $j\le N$ by letting $\abs{s}\to\infty$ along the positive real axis.

:::

:::

::: {.pf-step #reflection}
For all $s$ in the slit plane,
$$
F(s)F(-s)=\frac{1}{1-e^{2\pi is}}\ \text{ if }\ \Im(s)>0,
\qquad
F(s)F(-s)=\frac{1}{1-e^{-2\pi is}}\ \text{ if }\ \Im(s)<0 .
$$

::: pf-proof
By Theorem 1.4 of Chapter 6 (printed p. 164) and Lemma 1.2 of Chapter 6, $\Gamma(s)\Gamma(1-s)=\pi/\sin\pi s$ and $\Gamma(1-s)=-s\Gamma(-s)$, hence
$$
\Gamma(s)\Gamma(-s)=\frac{\pi}{-s\sin\pi s},
\tag{$\ast$}
$$
which is identity (14) of the text, printed p. 327. Assume first that $\Im(s)>0$, so that $\theta=\arg s\in(0,\pi)$; then $-s$ has argument $\theta-\pi\in(-\pi,0)$, and therefore
$$
\log(-s)=\log s-i\pi,\qquad (-s)^{1/2}=s^{1/2}e^{-i\pi/2}=-i\,s^{1/2}.
$$
Using these and $(\ast)$,
$$
F(s)F(-s)=\frac{\Gamma(s)\Gamma(-s)}{2\pi}\,s^{1/2}(-s)^{1/2}\,e^{-s\log s+s+s\log(-s)-s}
=\frac{-\pi}{2\pi s\sin\pi s}\,(-i)s\,e^{-i\pi s}
=\frac{i\,e^{-i\pi s}}{2\sin\pi s},
$$
and $2\sin\pi s=(e^{i\pi s}-e^{-i\pi s})/i$ gives $\frac{ie^{-i\pi s}}{2\sin\pi s}=-\frac{e^{-i\pi s}}{e^{i\pi s}-e^{-i\pi s}}=-\frac{1}{e^{2\pi is}-1}=\frac{1}{1-e^{2\pi is}}$. For $\Im(s)<0$ apply the result just proved to $\overline s$ (which has positive imaginary part) and conjugate, using $\overline{F(s)}=F(\overline{s})$ (the principal branches of $\log$ and of the square root are symmetric) and $\overline{1/(1-e^{2\pi i\overline s})}=1/(1-e^{-2\pi is})$; this gives the second identity. Both identities can also be read off from the single meromorphic identity obtained by continuing the first one across the real axis, which multiplies $1-e^{2\pi is}$ by no factor but replaces $F(-s)$ by the continuation of $F$ past the cut, which is why the two cases differ.

:::

:::

::: {.pf-step #left}
For $s\in S_\delta$ with $\Re(s)<0$ and $\abs{s}\ge4$, and for every integer $N\ge1$,
$$
F(s)=\frac{1}{\Psi_N(-1/s)}+O\bigl(\abs{s}^{-N}\bigr),
$$
uniformly on $\{s\in S_\delta:\Re(s)\le0,\ \abs{s}\ge4\}$.

::: pf-proof
Such $s$ satisfy $\Re(-s)>0$, so by step [](#recurrence){.pf-ref} applied at $-s$, $F(-s)=\Psi_N(-1/s)+O(\abs{s}^{-N})$, and $\Psi_N(-1/s)\to1$ as $\abs{s}\to\infty$, so $\Psi_N(-1/s)\ge1/2$ for $\abs{s}\ge R$ and $1/F(-s)=1/\Psi_N(-1/s)+O(\abs{s}^{-N})$. By step [](#reflection){.pf-ref}, $F(s)=1/\bigl((1-e^{2\pi is})F(-s)\bigr)$.

By step [](#reflection){.pf-ref}, $F(s)=1/\bigl(\varepsilon(s)F(-s)\bigr)$ with $\varepsilon(s)=1-e^{2\pi is}$ if $\Im(s)>0$ and $\varepsilon(s)=1-e^{-2\pi is}$ if $\Im(s)<0$. In both cases $\abs{e^{\mp2\pi is}}=e^{-2\pi\abs{\Im s}}$, and $\abs{\Im s}=\abs{s}\abs{\sin(\arg s)}\ge\abs{s}\sin\delta$ for $s\in S_\delta$ because $\abs{\arg s}\le\pi-\delta$; thus $e^{-2\pi\abs{\Im s}}\le e^{-2\pi\abs{s}\sin\delta}\le c_\delta<1$ for $\abs{s}\ge4$, so $\abs{1/\varepsilon(s)}\le1/(1-c_\delta)$ and $1/\varepsilon(s)=1+O(e^{-2\pi\abs{\Im s}})=1+O(\abs{s}^{-N})$ for every $N$. Multiplying the two estimates gives $F(s)=1/\Psi_N(-1/s)+O(\abs{s}^{-N})$.

:::

:::

::: {.pf-step #identify}
$\Psi_N(u)\Psi_N(-u)=1+O\bigl(\abs{u}^{N+1}\bigr)$ as $u\to0$, and consequently
$$
F(s)=\Psi_N(1/s)+O\bigl(\abs{s}^{-N}\bigr)\qquad\text{for } s\in S_\delta,\ \Re(s)<0,\ \abs{s}\ge4 .
$$

::: pf-proof
If $\delta>\pi/2$ then $S_\delta\subset\{\Re(s)>0\}$ and there is nothing to prove, so assume $\delta\le\pi/2$; then the imaginary axis lies in $S_\delta$, and every $it$ with $t\ge4$ belongs to the sets on which the estimates of steps [](#recurrence){.pf-ref} and [](#left){.pf-ref} are uniform.
Let $t\ge4$ and put $s=it$. By step [](#recurrence){.pf-ref}, $F(it)=\Psi_N(1/(it))+O(t^{-N})=\Psi_N(-i/t)+O(t^{-N})$. On the other hand, $\Re(s)\le0$ and the estimates of step [](#left){.pf-ref} are uniform on that set; taking the limit of the identity of step [](#left){.pf-ref} along $s\to it$ with $\Re(s)<0$ (both sides being continuous at $it\ne0$) gives $F(it)=1/\Psi_N(-1/(it))+O(t^{-N})=1/\Psi_N(i/t)+O(t^{-N})$.
Subtracting, $\Psi_N(-i/t)-1/\Psi_N(i/t)=O(t^{-N})$. Write $1/\Psi_N(u)=\sum_{j=0}^{N}b_ju^{j}+O(u^{N+1})$ for $\abs{u}\le1/2$, which exists because $\Psi_N(0)=1$; then $1/\Psi_N(i/t)=\sum_{j=0}^{N}b_ji^{j}t^{-j}+O(t^{-N-1})$ and $\Psi_N(-i/t)=\sum_{j=0}^{N}a_j(-i)^{j}t^{-j}+O(t^{-N-1})$, so
$$
\sum_{j=0}^{N}\bigl(a_j(-i)^{j}-b_ji^{j}\bigr)t^{-j}=O(t^{-N}).
$$
Multiplying by $t^{n}$ and letting $t\to\infty$ gives $a_n(-i)^{n}=b_ni^{n}$ for $n=0,1,\dots,N$, that is $b_n=(-1)^{n}a_n$ for every $n\le N$; hence $1/\Psi_N(u)=\Psi_N(-u)+O(u^{N+1})$, and multiplying by $\Psi_N(u)$ yields $\Psi_N(u)\Psi_N(-u)=1+O(\abs{u}^{N+1})$.
Substituting this into step [](#left){.pf-ref}, with $u=-1/s$, gives $1/\Psi_N(-1/s)=\Psi_N(1/s)+O(\abs{s}^{-N-1})$, which proves the second assertion.

:::

:::

::: pf-qed
Let $N\ge1$ and let $\abs{s}\ge4$ with $s\in S_\delta$. If $\Re(s)\ge0$, step [](#recurrence){.pf-ref} gives $\Gamma(s)=e^{s\log s}e^{-s}\frac{\sqrt{2\pi}}{s^{1/2}}\bigl(1+\sum_{j=1}^{N}a_js^{-j}+O(s^{-N})\bigr)$; if $\Re(s)<0$, step [](#identify){.pf-ref} gives the same, since $F(s)=\Psi_N(1/s)+O(\abs{s}^{-N})$ translates into exactly that display. The constants $a_j$ are real and $a_1=1/12$ by step [](#coefficients){.pf-ref}. As for every $N>0$ one may take the integer $N$ above replaced by $\lceil N\rceil$, this is the assertion of the problem.

:::

:::

:::
