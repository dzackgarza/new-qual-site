::: {.solution}
Throughout, $\eta\in C^\infty(\RR)$ is supported in a finite interval $[-b,b]$ with $b>0$, and $\eta=1$ on $(-a,a)$ for some $0<a\le b$; put $\chi=1-\eta$, so that $\chi\equiv 0$ on $(-a,a)$ and $\chi\equiv 1$ on $(b,\infty)$. We write $s^{-m-1}$ for the branch of the power on $\CC\setminus(-\infty,0]$ that is positive on $(0,\infty)$, and $\Gamma$ for Euler's gamma function, so that $\Gamma(m+1)=\int_0^\infty e^{-t}t^m\,dt$ for $m>-1$ (Chapter 6, printed p. 160). Since $N>0$ is arbitrary, it suffices to prove, for each integer $n\ge 1$, the estimate $O(\abs{s}^{-n})$ with a constant depending only on $m$, $n$ and $\eta$; the assertion for a given $N$ then follows with $n=\max(1,\lceil N\rceil)$. All estimates below are uniform for $\Re(s)\ge 0$ and $\abs{s}\ge 1$, and $s\ne 0$.

::: pf

::: {.pf-step #cutoff}
Let $g\in C^\infty([0,\infty))$ vanish identically on $[0,a)$ and on $(b,\infty)$. Then for every integer $n\ge 0$ and every $s\neq 0$ with $\Re(s)\ge 0$,
$$
\abs{\int_0^\infty e^{-sx}g(x)\,dx}\ \le\ \abs{s}^{-n}\int_0^b\abs{g^{(n)}(x)}\,dx .
$$

::: pf-proof
Since $g$ is supported in $[0,b]$, the integral equals $\int_0^b e^{-sx}g(x)\,dx$. Because $g$ vanishes identically on a neighbourhood of $0$ and of $b$, every derivative $g^{(k)}$ vanishes at $x=0$ and at $x=b$. Since $e^{-sx}=-\frac1s\frac{d}{dx}\bigl(e^{-sx}\bigr)$, an integration by parts gives
$$
\int_0^b e^{-sx}g(x)\,dx=\Bigl[-\frac{e^{-sx}}{s}g(x)\Bigr]_0^b+\frac1s\int_0^b e^{-sx}g'(x)\,dx=\frac1s\int_0^b e^{-sx}g'(x)\,dx,
$$
the boundary term being zero. Iterating this $n$ times, again with all boundary terms zero, gives $\int_0^b e^{-sx}g(x)\,dx=(-1)^n s^{-n}\int_0^b e^{-sx}g^{(n)}(x)\,dx$. Since $\abs{e^{-sx}}=e^{-\Re(s)x}\le 1$ for $x\ge 0$ and $\Re(s)\ge 0$, the estimate follows.

:::

:::

::: {.pf-step #parta}
For $-1<m\le 0$ and every integer $n\ge 1$,
$$
\int_0^\infty e^{-sx}x^m\eta(x)\,dx=s^{-m-1}\Gamma(m+1)+O\bigl(\abs{s}^{-n}\bigr).
$$

::: pf-proof
For $\Re(s)>0$ the substitution $x=t/s$ (a change of variables along the ray $\{t/s:t>0\}$, both integrals being absolutely convergent because $m>-1$ and $\Re(s)>0$) gives the identity
$$
\int_0^\infty e^{-sx}x^m\,dx=s^{-m-1}\int_0^\infty e^{-t}t^m\,dt=s^{-m-1}\Gamma(m+1),
\tag{1}
$$
which is also the computation (5) of Proposition 1.2, printed p. 321.
Define
$$
D(s)=\int_0^\infty e^{-sx}x^m\eta(x)\,dx-s^{-m-1}\Gamma(m+1),\qquad T(s)=\int_0^\infty e^{-sx}x^m\chi(x)\,dx .
$$
By (1) and $\eta=1-\chi$ we have $D(s)=-T(s)$ for $\Re(s)>0$. The function $s\mapsto\int_0^\infty e^{-sx}x^m\eta(x)\,dx$ is entire, because $\eta$ is supported in $[0,b]$ and $x^m$ is integrable on $[0,b]$; the function $s\mapsto s^{-m-1}\Gamma(m+1)$ is holomorphic on the slit plane $\CC\setminus(-\infty,0]$, on which the principal branch of the power is defined; and $T$ is entire. Hence $D$ and $-T$ are both holomorphic on the slit plane and they agree on the non-empty open set $\{\Re(s)>0\}$, so by the identity theorem $D=-T$ on the whole slit plane. Since $\{\Re(s)\ge 0\}\setminus\{0\}$ lies in the slit plane, it remains to bound $T$.

The function $g_m(x)=x^m\chi(x)$, extended by $0$ for $x\le 0$, lies in $C^\infty([0,\infty))$: on $(0,\infty)$ it is a product of smooth functions, and on $[0,a)$ it vanishes identically, so all its derivatives vanish there. Its support is contained in $[0,b]$, and it vanishes identically on $[0,a)$. So step [](#cutoff){.pf-ref} gives, for every $n\ge 1$,
$$
\abs{T(s)}=\abs{\int_0^\infty e^{-sx}g_m(x)\,dx}\le\abs{s}^{-n}\int_0^b\abs{g_m^{(n)}(x)}\,dx ,
$$
and $\int_0^b\abs{g_m^{(n)}}$ is finite because $g_m\in C^\infty$ has compact support. Hence $\abs{D(s)}=\abs{T(s)}=O(\abs{s}^{-n})$.

:::

:::

::: {.pf-step #choose-k}
Let $m>-1$ and let $k\ge 0$ be the integer with $k-1<m\le k$. Then $-1<m-k\le 0$ and, with $c=\prod_{j=0}^{k-1}(m-j)$ (the empty product for $k=0$),
$$
\Bigl(\frac{d}{dx}\Bigr)^k\bigl(x^m\bigr)=c\,x^{m-k}\quad\text{for } x>0,
\qquad c\neq 0 .
$$
Moreover $k=0$ exactly when $-1<m\le0$.

::: pf-proof
The integer $k\ge0$ with $k-1<m\le k$ exists by the Archimedean property of $\RR$, and $k=0$ means $-1<m\le0$ while $k\ge1$ means $k-1<m$, i.e. $m>k-1\ge0$. Thus $k-1<m$ gives $m-k>-1$ and $m\le k$ gives $m-k\le0$. Differentiating the monomial $k$ times gives $\bigl(x^m\bigr)^{(k)}=m(m-1)\cdots(m-k+1)x^{m-k}=c\,x^{m-k}$ (for $k=0$ both sides are $x^m$). Every factor $m-j$ with $0\le j\le k-1$ is nonzero: when $k\ge1$ we have $m-j\ge m-k+1>0$. Hence $c\neq0$.

:::

:::

::: {.pf-step #reduced}
With $k\ge0$ and $c$ as in step [](#choose-k){.pf-ref}, and every integer $n\ge1$,
$$
\int_0^\infty e^{-sx}\Bigl(\frac{d}{dx}\Bigr)^k\bigl(x^m\bigr)\eta(x)\,dx=c\,\Gamma(m-k+1)\,s^{-m+k-1}+O\bigl(\abs{s}^{-n}\bigr).
$$

::: pf-proof
By step [](#choose-k){.pf-ref} the integrand is $c\,e^{-sx}x^{m-k}\eta(x)$, and $m-k\in(-1,0]$. Step [](#parta){.pf-ref} applies to the exponent $m-k$ and gives $\int_0^\infty e^{-sx}x^{m-k}\eta(x)\,dx=s^{-(m-k)-1}\Gamma(m-k+1)+O(\abs{s}^{-n})=s^{-m+k-1}\Gamma(m-k+1)+O(\abs{s}^{-n})$; multiplying by $c$ gives the claim. (For $k=0$ this is step [](#parta){.pf-ref} itself.)

:::

:::

::: {.pf-step #ibp}
Fix $s\neq0$ and, for $0\le i\le k$, set
$$
F_i=\int_0^\infty e^{-sx}\bigl(x^m\bigr)^{(i)}(x)\,\eta(x)\,dx,
\qquad
G_i=\int_0^\infty e^{-sx}\bigl(x^m\bigr)^{(i)}(x)\,\eta'(x)\,dx .
$$
All these integrals converge absolutely. Moreover
$$
F_k=s^kF_0-\sum_{i=0}^{k-1}s^{k-1-i}G_i,
\qquad\text{and}\qquad G_i=O\bigl(\abs{s}^{-n}\bigr)\ \text{for every } n\ge 0 .
$$

::: pf-proof
That the $F_i$ converge follows from $\bigl(x^m\bigr)^{(i)}=c_i x^{m-i}$ with $m-i\ge m-k>-1$ and $\eta$ supported in $[0,b]$; the $G_i$ converge because $\eta'$ is supported in $[a,b]$ and $x^{m-i}$ is bounded there when $m-i\ge 0$, and integrable there when $m-i<0$. (For $k=0$ the assertions are $F_0=F_0$ and, for each $i$, the $G_i$ estimate below.)

For $1\le i\le k$ integrate by parts with $u=e^{-sx}\eta(x)$, $v=\bigl(x^m\bigr)^{(i-1)}$, so that $du=\bigl(-se^{-sx}\eta(x)+e^{-sx}\eta'(x)\bigr)dx$. Since $\eta$ vanishes identically on $(b,\infty)$ and $\bigl(x^m\bigr)^{(i-1)}=c_{i-1}x^{m-i+1}$ with $m-i+1\ge m-k+1>0$, the boundary term $\bigl[e^{-sx}\eta(x)\bigl(x^m\bigr)^{(i-1)}(x)\bigr]_0^\infty$ vanishes: at $x\to\infty$ because $\eta$ is eventually $0$, and at $x=0$ because $x^{m-i+1}\to0$. Hence
$$
F_i=sF_{i-1}-G_{i-1}\qquad(1\le i\le k).
$$
Iterating this relation gives $F_k=s^kF_0-\sum_{i=0}^{k-1}s^{k-1-i}G_i$: indeed, for $k=1$ it is the relation itself, and for $k>1$ we have $F_k=sF_{k-1}-G_{k-1}=s\bigl(s^{k-1}F_0-\sum_{i=0}^{k-2}s^{k-2-i}G_i\bigr)-G_{k-1}=s^kF_0-\sum_{i=0}^{k-1}s^{k-1-i}G_i$.

Finally, fix $i$ and put $g_i=\bigl(x^m\bigr)^{(i)}\eta'$. Since $\eta'$ vanishes identically on $[0,a)$ and on $(b,\infty)$, and $x^{m-i}$ is smooth on $(0,\infty)$, the function $g_i$, extended by $0$ outside $[a,b]$, lies in $C^\infty([0,\infty))$, is supported in $[0,b]$ and vanishes identically on $[0,a)$. So step [](#cutoff){.pf-ref} gives $\abs{G_i}\le\abs{s}^{-n}\int_0^b\abs{g_i^{(n)}}$, and the integral is finite. This holds for every $n\ge0$.

:::

:::

::: {.pf-step #partb}
For every $m>-1$ and every integer $n\ge 1$,
$$
\int_0^\infty e^{-sx}x^m\eta(x)\,dx=s^{-m-1}\Gamma(m+1)+O\bigl(\abs{s}^{-n}\bigr).
$$

::: pf-proof
Fix $m>-1$ and $k$, $c$ as in step [](#choose-k){.pf-ref}. Step [](#ibp){.pf-ref} gives $F_0=s^{-k}\bigl(F_k+\sum_{i=0}^{k-1}s^{k-1-i}G_i\bigr)=s^{-k}F_k+O\bigl(\abs{s}^{-n-1}\bigr)$, because $s^{-k}s^{k-1-i}=s^{-1-i}$ and $\abs{s}\ge1$. Substituting the expansion of $F_k$ from step [](#reduced){.pf-ref},
$$
F_0=s^{-k}\bigl(c\,\Gamma(m-k+1)s^{-m+k-1}+O(\abs{s}^{-n})\bigr)+O\bigl(\abs{s}^{-n-1}\bigr)
=c\,\Gamma(m-k+1)s^{-m-1}+O\bigl(\abs{s}^{-n}\bigr).
$$
By Lemma 1.2 of Chapter 6 (printed p. 161), $\Gamma(w+1)=w\Gamma(w)$; applied $k$ times, with all arguments $m-k+1,\dots,m$ lying in $\{\Re(w)>0\}$ because $m-k+1>0$, it gives $\Gamma(m+1)=m(m-1)\cdots(m-k+1)\Gamma(m-k+1)=c\,\Gamma(m-k+1)$. This proves the claim.

:::

:::

::: pf-qed
Step [](#parta){.pf-ref} proves assertion (a) of the problem, and step [](#partb){.pf-ref} proves assertion (b). Together they give, for every $m>-1$, every integer $n\ge1$ and all $s$ with $\Re(s)\ge0$, $\abs{s}\ge1$,
$$
\Bigl|\int_0^\infty e^{-sx}x^m\eta(x)\,dx-s^{-m-1}\Gamma(m+1)\Bigr|\le C_{m,n,\eta}\abs{s}^{-n},
$$
and choosing $n=\max(1,\lceil N\rceil)$ for the given $N>0$ yields $\int_0^\infty e^{-sx}x^m\eta(x)\,dx=s^{-m-1}\Gamma(m+1)+O(s^{-N})$ as $\abs{s}\to\infty$ in the closed half-plane $\Re(s)\ge0$, as required.

:::

:::

:::
