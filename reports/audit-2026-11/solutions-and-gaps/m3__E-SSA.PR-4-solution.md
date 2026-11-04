::: {.solution}
**Notation, and two corrections to the printed statement.** Write $\DD=\{w:\abs w<1\}$, and let $\Omega\supset\overline{\DD}$ be a region on which $F$ is meromorphic, the poles of $F$ being exactly the distinct points $\alpha_1,\dots,\alpha_k\in\partial\DD$, of orders $r_1,\dots,r_k$. The series in the problem is $F(w)=\sum_{n\ge0}F_nw^n$ (the letter $z$ of the printed statement is the same variable; we use $w$ for it).

(i) *Sign.* The displayed formula for $P_j$ needs a minus sign in front: $P_j$ is **minus** the residue of $w\mapsto F(w)w^{-n-1}$ at $\alpha_j$, as in (2) below. Check with $F(w)=1/(w-1)$, $k=1$, $\alpha_1=1$, $r_1=1$: here $F_n=-1$ for every $n$, while $\operatorname{res}_{w=1}\bigl(F(w)w^{-n-1}\bigr)=1$. With the residue itself in place of $P_1$ the asserted expansion fails for every $n$, so the minus sign is part of the statement.

(ii) *The factor $\alpha_j^{-n}$.* $P_j(n)$ is not a polynomial in $n$: it equals $\alpha_j^{-n}$ times a polynomial in $n$ of degree $r_j-1$, see (3). For $\abs{\alpha_j}=1$ that factor cannot be absorbed, and "each $P_j$ is a polynomial of degree $r_j-1$" is false as it stands: for $F(w)=1/(w-i)$ (a single simple pole at $\alpha_1=i$) one has $F_n=i(-i)^n$, which takes the four values $i,1,-i,-1$ periodically; if $F_n=P(n)+O(e^{-\epsilon n})$ with a polynomial $P$ (here necessarily constant, $P\equiv c$), then $i(-i)^n\to c$, which a non-constant periodic sequence cannot do. If all $\alpha_j=1$, then $P_j$ is literally a polynomial of degree $r_j-1$, by (3).

Statement proved below, for the $P_j$ defined in (2): there is $\epsilon>0$ with
$$
F_n=\sum_{j=1}^{k}P_j(n)+O(e^{-\epsilon n})\qquad(n\to\infty),
$$
and each $P_j$ has the form (3), so in particular $P_j(n)=\alpha_j^{-n}\bigl(A_jn^{r_j-1}+O(n^{r_j-2})\bigr)$ with $A_j\neq0$.

*Step 1: a disc of radius $>1$ carrying no poles except the $\alpha_j$.* $\overline{\DD}$ is compact and contained in the open set $\Omega$, so $\delta_0:=\operatorname{dist}(\overline{\DD},\CC\setminus\Omega)>0$. Put $\rho:=1+\delta_0/2>1$ and $D_\rho:=\{\abs w<\rho\}$; then $\overline{D_\rho}\subset\Omega$. Since the poles of $F$ in $\Omega$ are exactly the points $\alpha_j$, all of modulus $1$, the function $F$ is holomorphic on $D_\rho\setminus\{\alpha_1,\dots,\alpha_k\}$.

*Step 2: the residues give the coefficients.* For $n\ge0$ put $H_n(w)=F(w)w^{-n-1}$. On $D_\rho$ the function $H_n$ is holomorphic except for a pole of order $n+1$ at $0$ and a pole of order $r_j$ at each $\alpha_j$ (a pole of order $r_j$ because $F$ has one there and $w^{-n-1}$ is holomorphic and nonzero at $\alpha_j$). The residue formula for a circle with finitely many poles inside (Chapter 3, Corollary 2.2) applied to $H_n$ and the circle $\{\abs w=\rho\}$ gives
$$
\frac1{2\pi i}\oint_{\abs w=\rho}H_n(w)\,dw=\operatorname{res}_{0}H_n+\sum_{j=1}^{k}\operatorname{res}_{\alpha_j}H_n=F_n+\sum_{j=1}^{k}\operatorname{res}_{\alpha_j}H_n, \qquad(1)
$$
the last equality because the coefficient of $w^{-1}$ in the Laurent expansion of $F(w)w^{-n-1}$ at $0$ is by definition the coefficient of $w^{n}$ in the Taylor expansion of $F$ at $0$, namely $F_n$. On $\abs w=\rho$ the function $F$ is continuous (it is holomorphic near that circle), so $M:=\sup_{\abs w=\rho}\abs F<\infty$, and
$$
\Bigl|\frac1{2\pi i}\oint_{\abs w=\rho}H_n(w)\,dw\Bigr|\le\frac1{2\pi}\cdot2\pi\rho\cdot M\rho^{-n-1}=M\rho^{-n}=Me^{-\epsilon n},\qquad \epsilon:=\log\rho>0
$$
— here $\epsilon$ depends only on $F$, not on $n$. Combining with (1),
$$
F_n=\sum_{j=1}^{k}P_j(n)+O(e^{-\epsilon n}),\qquad
P_j(n):=-\operatorname{res}_{\alpha_j}\bigl(F(w)w^{-n-1}\bigr). \qquad(2)
$$

*Step 3: computing $P_j$.* By Chapter 3, Theorem 1.4 (the residue at a pole of order $r$), applied to $H_n$ at $\alpha_j$,
$$
P_j(n)=-\frac{1}{(r_j-1)!}\Bigl(\frac{d}{dw}\Bigr)^{r_j-1}\Bigl[(w-\alpha_j)^{r_j}F(w)\,w^{-n-1}\Bigr]_{w=\alpha_j}. \qquad(2')
$$
This is the formula displayed in the problem, with the minus sign of (i).

*Step 4: $P_j$ is $\alpha_j^{-n}$ times a polynomial of degree $r_j-1$.* Put $G_j(w)=(w-\alpha_j)^{r_j}F(w)$, holomorphic in a disc around $\alpha_j$ and satisfying $G_j(\alpha_j)\neq0$ (the pole has order exactly $r_j$). By Leibniz and (2'),
$$
P_j(n)=-\sum_{i=0}^{r_j-1}\frac{G_j^{(i)}(\alpha_j)}{i!\,(r_j-1-i)!}\Bigl[\Bigl(\frac{d}{dw}\Bigr)^{r_j-1-i}w^{-n-1}\Bigr]_{w=\alpha_j},
$$
and $\bigl(\frac{d}{dw}\bigr)^{s}w^{-n-1}=(-1)^{s}(n+1)(n+2)\cdots(n+s)w^{-n-1-s}$ for $s\ge0$. As $\abs{\alpha_j}=1$, the $i$-th summand is
$$
-\frac{G_j^{(i)}(\alpha_j)}{i!\,(r_j-1-i)!}(-1)^{r_j-1-i}\prod_{t=1}^{r_j-1-i}(n+t)\ \alpha_j^{-n}\alpha_j^{-1-(r_j-1-i)},
$$
a polynomial in $n$ of degree $r_j-1-i$ times $\alpha_j^{-n}$. Therefore
$$
P_j(n)=\alpha_j^{-n}Q_j(n), \qquad Q_j \text{ a polynomial of degree } r_j-1 \text{ with leading coefficient }
A_j=\frac{(-1)^{r_j}G_j(\alpha_j)}{(r_j-1)!}\,\alpha_j^{-r_j}\neq0, \qquad(3)
$$
the leading term coming from $i=0$, where $\prod_{t=1}^{r_j-1}(n+t)=n^{r_j-1}+O(n^{r_j-2})$ and $G_j(\alpha_j)\neq0$. In particular $\abs{P_j(n)}\le C\,n^{r_j-1}$, and $P_j(n)=\alpha_j^{-n}\bigl(A_jn^{r_j-1}+O(n^{r_j-2})\bigr)$.

*Step 5: conclusion.* Substituting (3) into (2) gives the asserted expansion, with $\epsilon=\log\rho>0$ from Step 2 and $P_j$ as in (2'); each $P_j$ is $\alpha_j^{-n}$ times a polynomial of degree exactly $r_j-1$.

*Checks.* (a) $F(w)=1/(w-1)^2$: here $k=1$, $\alpha_1=1$, $r_1=2$, $F_n=n+1$, and (2') gives $P_1(n)=-\frac{d}{dw}\bigl[w^{-n-1}\bigr]_{w=1}=n+1$. (b) $F(w)=\frac{1}{(w-1)^2(w+1)}$: the poles are $1$ (order $2$) and $-1$ (order $1$); partial fractions give $F_n=\frac n2+\frac34+\frac{(-1)^n}{4}$, while (2') and (3) give $P_1(n)=\frac n2+\frac34=\alpha_1^{-n}Q_1(n)$ and $P_2(n)=\frac{(-1)^n}{4}=\alpha_2^{-n}Q_2(n)$, with $\deg Q_1=1=r_1-1$ and $\deg Q_2=0=r_2-1$. (c) $F(w)=1/(w-i)$: $F_n=i(-i)^n=P_1(n)$ exactly — by Step 2, $F_n-P_1(n)=O(e^{-\epsilon n})$ for every $\epsilon>0$, since $F$ is meromorphic on $\CC$ and $\rho$ may be taken arbitrarily large; letting $\epsilon\to\infty$ for fixed $n$ gives $F_n=P_1(n)$.
:::
