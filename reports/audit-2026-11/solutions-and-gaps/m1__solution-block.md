::: {.solution}

Let $M>0$, let $h\colon[-M,M]\to\CC$ be continuous, put $B\coloneqq\sup_{[-M,M]}\abs{h}$, and set

$$
g(z)\coloneqq\frac{1}{2\pi i}\int_{-M}^{M}\frac{h(y)}{y-z}\,dy,\qquad z\in\Omega\coloneqq\CC\setminus[-M,M].
$$

The only results of the book used below are Theorem 5.4, Theorem 5.5 and Corollary 4.5 of Chapter 2, and Theorem 3.1 and Corollary 4.6 of Chapter 3 [@SS03]. The two elementary lemmas they are applied through are proved first. Nothing about the behaviour of $h$ at the endpoints $\pm M$ is assumed unless it is stated.

**Lemma 1 (the Poisson kernel of the half-plane).** For $\varepsilon>0$ and $t\in\RR$ put $P_\varepsilon(t)\coloneqq\frac{1}{\pi}\frac{\varepsilon}{t^2+\varepsilon^2}$. Then $\int_\RR P_\varepsilon(t)\,dt=1$, and for every $\gamma>0$

$$
\int_{\abs{t}>\gamma}P_\varepsilon(t)\,dt=\frac{2}{\pi}\arctan\frac{\varepsilon}{\gamma}\longrightarrow0\qquad(\varepsilon\to0^+).
$$

*Proof.* The substitution $t=\varepsilon u$ gives $\int_\RR P_\varepsilon=\frac1\pi\int_\RR\frac{du}{1+u^2}=1$ and $\int_{\abs{t}>\gamma}P_\varepsilon=\frac1\pi\int_{\abs{u}>\gamma/\varepsilon}\frac{du}{1+u^2}=1-\frac{2}{\pi}\arctan\frac{\gamma}{\varepsilon}=\frac{2}{\pi}\arctan\frac{\varepsilon}{\gamma}$, using $\arctan(1/s)=\frac\pi2-\arctan s$ for $s>0$. $\square$

**Lemma 2 (approximate identity on the line).** Let $H\colon\RR\to\CC$ be continuous, bounded by $B$, and uniformly continuous; for instance $H$ the extension of $h$ by $0$ outside $[-M,M]$, which is uniformly continuous as soon as $h$ satisfies the Hölder condition of part (b) and $h(\pm M)=0$. Then

$$
\sup_{x\in\RR}\abs{\int_\RR P_\varepsilon(y-x)H(y)\,dy-H(x)}\longrightarrow0\qquad(\varepsilon\to0^+).
$$

*Proof.* Fix $\eta>0$ and choose $\gamma>0$ with $\abs{H(y)-H(x)}<\eta$ whenever $\abs{y-x}<\gamma$, uniformly in $x$ by uniform continuity. Then, since $\int_\RR P_\varepsilon=1$,

$$
\abs{\int_\RR P_\varepsilon(y-x)H(y)dy-H(x)}
\le\int_{\abs{y-x}<\gamma}P_\varepsilon(y-x)\eta\,dy+2B\int_{\abs{y-x}\ge\gamma}P_\varepsilon(y-x)\,dy
\le\eta+2B\cdot\frac{2}{\pi}\arctan\frac{\varepsilon}{\gamma},
$$

by Lemma 1, and the right side is $<\eta+2B\cdot\frac{2}{\pi}\frac{\varepsilon}{\gamma}$ for all $x$ at once. $\square$

**Part (a): holomorphy, vanishing at infinity, and the jump.**

**Step 1: $g$ is holomorphic on $\Omega$.** The substitution $y=-M+2Ms$ turns the integral into an integral over $[0,1]$:

$$
g(z)=\frac{M}{\pi i}\int_0^1\frac{h(-M+2Ms)}{-M+2Ms-z}\,ds=\frac{M}{\pi i}\int_0^1F(z,s)\,ds,
\qquad F(z,s)\coloneqq\frac{h(-M+2Ms)}{-M+2Ms-z}.
$$

For each $s\in[0,1]$ the denominator $-M+2Ms-z$ is a non-zero holomorphic function of $z$ on $\Omega$ (its zero $-M+2Ms$ lies on $[-M,M]$), so $F(\cdot,s)$ is holomorphic on $\Omega$; and $F$ is continuous on $\Omega\times[0,1]$, because $h$ is continuous on $[-M,M]$ and $\abs{-M+2Ms-z}$ is continuous and nowhere zero there. By Theorem 5.4 of Chapter 2 [@SS03] the integral is holomorphic on $\Omega$.

**Step 2: $g$ vanishes at infinity.** If $\abs{z}\ge2M$ and $\abs{y}\le M$ then $\abs{y-z}\ge\abs{z}-M\ge\abs{z}/2$, hence

$$
\abs{g(z)}\le\frac{1}{2\pi}\int_{-M}^{M}\frac{\abs{h(y)}}{\abs{y-z}}\,dy\le\frac{1}{2\pi}\cdot 2M\cdot\frac{B}{\abs{z}/2}=\frac{2MB}{\pi\abs{z}},
$$

so $\abs{g(z)}\to0$ as $\abs{z}\to\infty$; in particular $g$ is bounded on $\Omega$.

**Step 3: the jump.** For $x\in\RR$, $\varepsilon>0$ and $y\ne x$,

$$
\frac{1}{y-x-i\varepsilon}-\frac{1}{y-x+i\varepsilon}
=\frac{(y-x+i\varepsilon)-(y-x-i\varepsilon)}{(y-x)^2+\varepsilon^2}
=\frac{2i\varepsilon}{(y-x)^2+\varepsilon^2},
$$

so, by the definition of $g$ and the definition of $P_\varepsilon$,

$$
g(x+i\varepsilon)-g(x-i\varepsilon)
=\frac{1}{2\pi i}\int_{-M}^{M}h(y)\,\frac{2i\varepsilon}{(y-x)^2+\varepsilon^2}\,dy
=\int_{-M}^{M}P_\varepsilon(y-x)h(y)\,dy .
$$

Fix $0<\delta<M$ and $x\in[-M+\delta,M-\delta]$. Since $[-M,M]\supseteq[x-\delta,x+\delta]$,

$$
0\le 1-\int_{-M}^{M}P_\varepsilon(y-x)\,dy\le\int_{\abs{t}>\delta}P_\varepsilon(t)\,dt=\frac{2}{\pi}\arctan\frac{\varepsilon}{\delta}\longrightarrow0 ,
$$

and with $\gamma>0$ chosen so that $\abs{h(y)-h(x)}<\eta$ for $\abs{y-x}<\gamma$ (possible uniformly in $x$ because $h$ is uniformly continuous on the compact interval $[-M,M]$),

$$
\Bigl|\int_{-M}^{M}P_\varepsilon(y-x)h(y)dy-h(x)\Bigr|
\le\eta+2B\int_{\abs{t}>\gamma}P_\varepsilon(t)\,dt+B\int_{\abs{t}>\delta}P_\varepsilon(t)\,dt .
$$

Hence the convergence holds uniformly on $[-M+\delta,M-\delta]$. This proves

$$
h(x)=\lim_{\substack{\varepsilon\to0\\ \varepsilon>0}}\bigl(g(x+i\varepsilon)-g(x-i\varepsilon)\bigr)
\qquad\text{for every }x\in(-M,M),
$$

uniformly on compact subsets of $(-M,M)$.

**The endpoints.** The same computation locates the limit at $x=\pm M$: with $y=M-u$,

$$
g(M+i\varepsilon)-g(M-i\varepsilon)=\frac{1}{\pi}\int_{0}^{2M}\frac{\varepsilon}{u^2+\varepsilon^2}h(M-u)\,du
\longrightarrow h(M)\cdot\frac{1}{\pi}\int_0^\infty\frac{du}{1+u^2}=\frac{h(M)}{2},
$$

and likewise at $-M$. So the printed identity "the jump of $g$ across $[-M,M]$ is $h$" holds on the open interval only: at an endpoint the segment bounds $\Omega$ from one side, half of the kernel mass falls outside $[-M,M]$, and the limit of the difference is $h(\pm M)/2$. On the open interval, where the jump is two-sided, the identity is exactly as printed.

**Part (b): boundary values under a Hölder condition, and the characterisation.**

From now on $h$ satisfies the Hölder condition of the statement: there are $C>0$ and $0<\alpha\le1$ with $\abs{h(y)-h(x)}\le C\abs{y-x}^{\alpha}$ for all $x,y\in[-M,M]$.

**Step 4: the Plemelj formula, uniformly on compact subsets of the open interval.** For $x\in(-M,M)$ set

$$
A(x)\coloneqq\operatorname{PV}\!\int_{-M}^{M}\frac{h(y)}{y-x}\,dy,\qquad
g^{\pm}(x)\coloneqq\pm\frac{h(x)}{2}+\frac{1}{2\pi i}A(x).
$$

Then $A(x)$ is a well-defined finite number and

$$
g(x+i\varepsilon)\longrightarrow g^{+}(x),\qquad g(x-i\varepsilon)\longrightarrow g^{-}(x)
\qquad(\varepsilon\to0^+),
$$

uniformly on $[-M+\delta,M-\delta]$ for every $0<\delta<M$. In particular $g^{+}-g^{-}=h$ on $(-M,M)$.

*Proof.* Write $K_\varepsilon(u)\coloneqq u/(u^2+\varepsilon^2)$. For $x\in(-M,M)$, $\varepsilon>0$,

$$
\frac{1}{(y-x)-i\varepsilon}=\frac{(y-x)+i\varepsilon}{(y-x)^2+\varepsilon^2},
$$

so with $A_\varepsilon(x)\coloneqq\int_{-M}^{M}h(y)K_\varepsilon(y-x)\,dy$ and $B_\varepsilon(x)\coloneqq\varepsilon\int_{-M}^{M}\frac{h(y)}{(y-x)^2+\varepsilon^2}\,dy$,

$$
g(x+i\varepsilon)=\frac{1}{2\pi i}\bigl(A_\varepsilon(x)+iB_\varepsilon(x)\bigr),
\qquad
B_\varepsilon(x)=\pi\int_{-M}^{M}P_\varepsilon(y-x)h(y)\,dy .
$$

*(i) $A$ exists.* Since $\abs{\frac{h(y)-h(x)}{y-x}}\le C\abs{y-x}^{\alpha-1}$ is integrable on $[-M,M]$, and since $\operatorname{PV}\int_{-M}^M\frac{dy}{y-x}=\log\frac{M-x}{M+x}$ for $\abs{x}<M$ (the primitive is $\log\abs{y-x}$; the two sides give $\log(M-x)-\log(M+x)$),

$$
A(x)=\int_{-M}^{M}\frac{h(y)-h(x)}{y-x}\,dy+h(x)\log\frac{M-x}{M+x},
$$

so $A(x)$ is finite, and $A$ is continuous on $(-M,M)$ by dominated convergence.

*(ii) $B_\varepsilon\to\pi h$.* This is the estimate of Step 3: for $x\in[-M+\delta,M-\delta]$,

$$
\Bigl|\frac{B_\varepsilon(x)}{\pi}-h(x)\Bigr|\le\eta(\gamma)+2B\int_{\abs{t}>\gamma}P_\varepsilon(t)\,dt+B\int_{\abs{t}>\delta}P_\varepsilon(t)\,dt
$$

with $\eta(\gamma)\coloneqq\sup\{\abs{h(y)-h(x)}:\abs{y-x}<\gamma\}$, which tends to $0$ with $\gamma$ uniformly in $x$ by uniform continuity of $h$ on $[-M,M]$.

*(iii) $A_\varepsilon\to A$.* Put $J_\varepsilon(x)\coloneqq\int_{-M}^{M}K_\varepsilon(y-x)\,dy=\frac12\log\frac{(M-x)^2+\varepsilon^2}{(M+x)^2+\varepsilon^2}$ and $J(x)\coloneqq\log\frac{M-x}{M+x}\ (=J_\varepsilon(x)$ with $\varepsilon=0)$. Subtracting the two expressions,

$$
A_\varepsilon(x)-A(x)=\int_{-M}^{M}\bigl(h(y)-h(x)\bigr)\Bigl(K_\varepsilon(y-x)-\frac{1}{y-x}\Bigr)dy+h(x)\bigl(J_\varepsilon(x)-J(x)\bigr).
$$

For $u\neq0$, $\bigl|K_\varepsilon(u)-\frac1u\bigr|=\frac{\varepsilon^2}{\abs{u}(u^2+\varepsilon^2)}\le\min\Bigl(\frac{2}{\abs{u}},\frac{\varepsilon^2}{\abs{u}^3}\Bigr)$; and for $\abs{x}\le M-\delta$, $\abs{J_\varepsilon(x)-J(x)}\le\frac12\Bigl(\frac{\varepsilon^2}{(M-x)^2}+\frac{\varepsilon^2}{(M+x)^2}\Bigr)\le\frac{\varepsilon^2}{\delta^2}$, using $\abs{\log(1+s)}\le s$ for $s\ge0$. Hence, for any $\gamma>0$ and $\abs{x}\le M-\delta$,

$$
\abs{A_\varepsilon(x)-A(x)}
\le C\!\int_{\abs{u}\le\gamma}\!2\abs{u}^{\alpha-1}du+2B\!\int_{\abs{u}>\gamma}\!\frac{\varepsilon^2}{\abs{u}^3}du+\frac{B\varepsilon^2}{\delta^2}
=\frac{4C\gamma^{\alpha}}{\alpha}+\frac{2B\varepsilon^2}{\gamma^2}+\frac{B\varepsilon^2}{\delta^2},
$$

independently of $x$. Letting first $\varepsilon\to0^+$ and then $\gamma\to0^+$ proves (iii). Combining (i)–(iii) gives the claim, since $g(x+i\varepsilon)-g^{+}(x)=\frac{1}{2\pi i}\bigl(A_\varepsilon(x)-A(x)\bigr)+\frac{1}{2\pi}\bigl(B_\varepsilon(x)-\pi h(x)\bigr)$; the computation for $g(x-i\varepsilon)$ and $g^{-}(x)$ is the same with $\varepsilon$ replaced by $-\varepsilon$. $\square$

So without any hypothesis at the endpoints $g$ has the two boundary functions $g^{\pm}$, and $g^{+}-g^{-}=h$, on the open interval, uniformly on compact subsets.

**Step 5: the boundary functions are uniform up to the endpoints when $h(\pm M)=0$.** Assume in addition $h(\pm M)=0$. Then the extension $H$ of $h$ by $0$ outside $[-M,M]$ satisfies the same Hölder inequality on all of $\RR$: for $y\in[-M,M]$ and $x>M$ one has $\abs{H(y)-H(x)}=\abs{h(y)}=\abs{h(y)-h(M)}\le C(y-M)^{\alpha}\le C\abs{y-x}^{\alpha}$, and symmetrically at $-M$. Consequently

$$
\sup_{x\in[-M,M]}\abs{g(x+i\varepsilon)-g^{+}(x)}\longrightarrow0,
\qquad
\sup_{x\in[-M,M]}\abs{g(x-i\varepsilon)-g^{-}(x)}\longrightarrow0
\qquad(\varepsilon\to0^+),
$$

where now $g^{\pm}(x)\coloneqq\pm\frac{h(x)}{2}+\frac{1}{2\pi i}A(x)$ and $A(x)\coloneqq\operatorname{PV}\int_\RR\frac{H(y)}{y-x}\,dy=\int_\RR\frac{H(y)-H(x)}{y-x}\,dy$; this $A$ agrees with the $A$ of Step 4 on $(-M,M)$, is continuous on $[-M,M]$, and $g^{\pm}(\pm M)$ are finite with $g^{+}(\pm M)=g^{-}(\pm M)=A(\pm M)/(2\pi i)$.

*Proof.* Because $\operatorname{PV}\int_\RR\frac{du}{u}=0$ (the symmetric limit of an odd integrand),

$$
A_\varepsilon(x)-A(x)=\int_\RR\bigl(H(y)-H(x)\bigr)\Bigl(K_\varepsilon(y-x)-\frac{1}{y-x}\Bigr)dy,
$$

the integrand now being integrable over all of $\RR$, and the estimate (iii) of Step 4, with $B$ the bound of $H$, applies verbatim and independently of $x$:

$$
\sup_{x\in\RR}\abs{A_\varepsilon(x)-A(x)}\le\frac{4C\gamma^{\alpha}}{\alpha}+\frac{2B\varepsilon^2}{\gamma^2}.
$$

Likewise $B_\varepsilon(x)=\pi\int_\RR P_\varepsilon(y-x)H(y)\,dy$ and Lemma 2 gives $\sup_{x\in\RR}\abs{B_\varepsilon(x)-\pi H(x)}\to0$. Both statements are uniform on $\RR$, hence on $[-M,M]$. $\square$

**Step 6: the characterisation.** Let $\mathcal{C}$ be the class of functions $G$ with

- (i) $G$ holomorphic on $\Omega$;
- (ii) $G(z)\to0$ as $\abs{z}\to\infty$;
- (iii) $G(x+i\varepsilon)$ and $G(x-i\varepsilon)$ converge as $\varepsilon\to0^+$, uniformly in $x\in[-M,M]$, to functions $G^{+},G^{-}$ continuous on $[-M,M]$ with $G^{+}-G^{-}=h$.

Then:

1. $\mathcal{C}$ has at most one element;
2. $g\in\mathcal{C}$ if and only if $h(\pm M)=0$. In particular, if $h$ vanishes at $\pm M$ — for instance if the support of $h$ is a compact subset of $(-M,M)$ — then $g$ is the unique holomorphic function satisfying (i), (ii), (iii), as the problem asserts.

*Proof of 1.* Let $G_1,G_2\in\mathcal{C}$ and put $H\coloneqq G_1-G_2$. Then $H$ is holomorphic on $\Omega$, $H(z)\to0$ as $\abs{z}\to\infty$, and $H(x\pm i\varepsilon)$ converge uniformly on $[-M,M]$ to $H^{\pm}\coloneqq G_1^{\pm}-G_2^{\pm}$, with $H^{+}-H^{-}=h-h=0$.

*(a) $H$ is holomorphic on $\CC\setminus\{M,-M\}$.* $H$ is holomorphic on the upper half-plane and on the lower half-plane, both of which lie in $\Omega$. It extends continuously to $I\coloneqq\RR\setminus\{\pm M\}$ from either side, and the two extensions agree on $I$: on $(-M,M)$ because $H^{+}-H^{-}=0$ there, and on $\{\abs{x}>M\}$ because $H$ is holomorphic, hence continuous, in a neighbourhood of such an $x$. The region $\CC\setminus\{M,-M\}$ has $I$ as its part on $\RR$; by Theorem 5.5 of Chapter 2 (the symmetry principle) [@SS03] the function glued from $H$ above and below $I$ is holomorphic on $\CC\setminus\{M,-M\}$.

*(b) $H$ is bounded near $\pm M$.* Fix $0<r<M$ and let $U\coloneqq\{z:\abs{z-M}<r,\ \operatorname{Im}z>0\}$. Then $H$ is holomorphic on $U$ and continuous on $\overline{U}$: on the diameter $(M-r,M+r)$ the limit from above is $H^{+}$, continuous on $[-M,M]$ and in particular at $x=M$, and on $(M,M+r)$ it is $H$ itself. So Corollary 4.6 of Chapter 3 (the maximum modulus principle on a region with compact closure) [@SS03] gives

$$
\sup_{z\in U}\abs{H(z)}\le\sup_{z\in\overline U\setminus U}\abs{H(z)}<\infty .
$$

The same argument with $\operatorname{Im}z<0$ bounds $H$ on $\{0<\abs{z-M}<r\}$, and $M$ may be replaced by $-M$.

*(c) $H$ is entire.* By Theorem 3.1 of Chapter 3 (Riemann's theorem on removable singularities) [@SS03] the bounded holomorphic function $H$ on the punctured discs at $M$ and at $-M$ extends holomorphically across both points.

*(d) $H\equiv0$.* $H$ is entire and $H(z)\to0$ as $\abs{z}\to\infty$, so $H$ is bounded; by Corollary 4.5 of Chapter 2 (Liouville's theorem) [@SS03] $H$ is constant, and its limit at infinity is $0$. Hence $G_1=G_2$. $\square$

*Proof of 2.* If $h(\pm M)=0$, Step 5 exhibits the limits, so $g\in\mathcal{C}$. Conversely let $h(M)\ne0$. Substituting $y=M-u$, $u\in[0,2M]$, and using $\abs{u+i\varepsilon}\ge\max(u,\varepsilon)$,

$$
g(M+i\varepsilon)=-\frac{1}{2\pi i}\int_0^{2M}\frac{h(M-u)}{u+i\varepsilon}\,du .
$$

Write $h(M-u)=h(M)+\rho(u)$ with $\abs{\rho(u)}\le Cu^{\alpha}$. Then $\bigl|\int_0^{2M}\frac{\rho(u)}{u+i\varepsilon}du\bigr|\le C\int_0^{2M}u^{\alpha-1}du=\frac{C(2M)^{\alpha}}{\alpha}$, while

$$
\int_0^{2M}\frac{du}{u+i\varepsilon}=\log(2M+i\varepsilon)-\log(i\varepsilon)=\log\frac{2M}{\varepsilon}-\frac{\pi i}{2}+o(1)\qquad(\varepsilon\to0^+).
$$

Hence

$$
\abs{g(M+i\varepsilon)}=\frac{\abs{h(M)}}{2\pi}\log\frac1\varepsilon+O(1)\longrightarrow\infty ,
$$

and the same holds at $-M$ and for $g(M-i\varepsilon)$. So $g(M+i\varepsilon)$ has no finite limit as $\varepsilon\to0^+$, and (iii) fails. $\square$

**Remarks on the printed statement.**

1. **The jump identity is an identity on the open interval.** On $(-M,M)$ it holds exactly as printed, and in fact uniformly on compact subsets (Steps 3 and 4). At $x=\pm M$ the limit of $g(x+i\varepsilon)-g(x-i\varepsilon)$ is $h(\pm M)/2$, because half of the mass of the kernel $P_\varepsilon$ falls outside $[-M,M]$; there the segment bounds $\Omega$ from one side only, so no two-sided jump exists.

2. **Condition (iii) is a statement about uniformity on the closed interval, and $g$ satisfies it precisely when $h(\pm M)=0$.** If $h(\pm M)\ne0$, Step 6 shows $g(M\pm i\varepsilon)$ grows like $\frac{\abs{h(M)}}{2\pi}\log\frac1\varepsilon$; the limits $g^{\pm}$ then exist only on the open interval (Step 4). Both versions are recorded above.

3. **The book's hint is exactly the endpoint hypothesis.** "If $G$ is another function satisfying these conditions, $g-G$ is entire" is the content of Step 6(a)–(c): the symmetry principle gives holomorphy away from $\pm M$, and it is the uniform convergence *on the closed interval* that makes $H$ continuous on the closed half-discs, whence bounded near $\pm M$ by the maximum modulus principle and removable by Riemann's theorem.

4. **That hypothesis cannot be dropped.** If (iii) is weakened to convergence uniformly on compact subsets of $(-M,M)$ — the conclusion of Step 4, which holds for every Hölder $h$ — the characterisation fails: then

$$
G(z)\coloneqq g(z)+\frac{1}{z^2-M^2}
$$

also satisfies (i) and (ii) (its only poles are at $\pm M\notin\Omega$), and $G(x\pm i\varepsilon)$ converge uniformly on compact subsets of $(-M,M)$ with $G^{+}-G^{-}=h$, since $\frac{1}{z^2-M^2}$ is continuous at every point of $(-M,M)$ and has the same limit from either side; yet $G\ne g$, and $G-g$ is not entire. So what singles $g$ out is the boundedness of $G-g$ near the two endpoints — the hypothesis that makes $G-g$ entire — and not condition (iii) alone.

:::
