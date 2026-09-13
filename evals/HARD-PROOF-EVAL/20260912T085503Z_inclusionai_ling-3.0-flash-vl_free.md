# Eval: inclusionai/ling-3.0-flash-vl:free

- Run timestamp (UTC): 20260912T085503Z
- Model timestamp (UTC): 20260912T091025Z
- Model: `inclusionai/ling-3.0-flash-vl:free`
- Provider: `inclusionai`
- Success: True
- Usage: {"prompt_tokens": 3717, "completion_tokens": 18339, "total_tokens": 22056, "cost": 0, "is_byok": false, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "cost_details": {"upstream_inference_cost": 0, "upstream_inference_prompt_cost": 0, "upstream_inference_completions_cost": 0}, "completion_tokens_details": {"reasoning_tokens": 9043, "image_tokens": 0, "audio_tokens": 0}}
- Problem source: `HARD-PROOF-EVAL.md` verbatim (Koebe-Bieberbach)
- Prompt length: 8778 chars
- Max tokens: per-model saturated (32768), timeout: none

---

## Chain-of-Thought (reasoning)

Let me work through each part (a) through (g) carefully and completely.

## Part (a): No uniform $r$ exists without further restrictions.

We need to find holomorphic functions $f_n: \mathbb{D} \to \mathbb{C}$ with $f_n(0) = 0$ such that $1/n \notin f_n(\mathbb{D})$.

Take $f_n(z) = z/n$. Then:
- $f_n(0) = 0$ ✓
- $f_n$ is holomorphic on $\mathbb{D}$ ✓
- $f_n(\mathbb{D}) = \{z/n : |z| < 1\} = D_{1/n}(0)$, the open disk of radius $1/n$ centered at 0.
- The point $1/n$ has modulus $1/n$, so $1/n \notin D_{1/n}(0)$ (since the disk is open).

Thus $1/n \notin f_n(\mathbb{D})$.

$f_n'(0) = 1/n \to 0$ as $n \to \infty$.

For any $r > 0$, choose $n$ large enough so that $1/n < r$. Then $1/n \in D_r(0)$ but $1/n \notin f_n(\mathbb{D})$, so $D_r(0) \not\subseteq f_n(\mathbb{D})$.

## Part (b): No uniform $r$ exists even with $f'(0) = 1$.

Consider $f_\epsilon(z) = \epsilon(e^{z/\epsilon} - 1)$ for $\epsilon > 0$.

- $f_\epsilon(0) = \epsilon(e^0 - 1) = 0$ ✓
- $f_\epsilon'(z) = e^{z/\epsilon}$, so $f_\epsilon'(0) = 1$ ✓
- $f_\epsilon$ is holomorphic on $\mathbb{D}$ (entire, in fact) ✓

Now, $e^{z/\epsilon} \neq 0$ for all $z \in \mathbb{C}$, so $f_\epsilon(z) = \epsilon(e^{z/\epsilon} - 1) \neq \epsilon(0 - 1) = -\epsilon$.

Thus $-\epsilon \notin f_\epsilon(\mathbb{D})$.

For any $r > 0$, choose $\epsilon < r$. Then $|-\epsilon| = \epsilon < r$, so $-\epsilon \in D_r(0)$, but $-\epsilon \notin f_\epsilon(\mathbb{D})$. Hence $D_r(0) \not\subseteq f_\epsilon(\mathbb{D})$.

## Part (c): Area theorem

Let $h(z) = \frac{1}{z} + c_0 + c_1 z + c_2 z^2 + \cdots$ be analytic and injective for $0 < |z| < 1$.

Consider $h$ restricted to $D_\rho(0) \setminus \{0\}$ for $0 < \rho < 1$. The image $h(D_\rho(0) \setminus \{0\})$ is an open set (by the open mapping theorem applied to $h$ on the annulus).

**Computing the area of the complement:**

The complement of $h(D_\rho(0) \setminus \{0\})$ in $\hat{\mathbb{C}}$ (or rather in $\mathbb{C}$, since $h$ maps the punctured disk to an unbounded set) can be computed using the area formula.

The boundary of $h(D_\rho(0) \setminus \{0\})$ includes the image of $|z| = \rho$. On $|z| = \rho$, we have:
$$h(z) = \frac{1}{z} + c_0 + c_1 z + c_2 z^2 + \cdots$$

The area of the complement of the image of the annulus $0 < |z| < \rho$ under $h$ can be computed as follows. Consider the map $w = h(z)$. The area of the complement of $h(D_\rho \setminus \{0\})$ in $\mathbb{C}$ is:

Using the formula for area via the Laurent series: if $h(z) = 1/z + \sum_{n=0}^{\infty} c_n z^n$, then the area of the complement of $h(D_\rho \setminus \{0\})$ is:

$$\text{Area}(\text{complement}) = \pi \left(\frac{1}{\rho^2} - \sum_{n=1}^{\infty} n |c_n|^2 \rho^{2n}\right)$$

Let me derive this more carefully. The area of the image of the annulus $\rho_1 < |z| < \rho_2$ under $h$ is given by:
$$\text{Area} = \iint_{\rho_1 < |z| < \rho_2} |h'(z)|^2 \, dx \, dy$$

But since $h$ is injective on this annulus, this equals the area of $h(\text{annulus})$.

Actually, let me use a different approach. Consider the complement of $h(D_\rho \setminus \{0\})$. Since $h$ maps the punctured disk to a domain whose complement is compact (because $h(z) \to \infty$ as $z \to 0$), we can compute the area of the complement.

For $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \cdots$, consider the inverse function. Near $\infty$, $h^{-1}(w)$ behaves like $1/w$. The complement of $h(D_\rho \setminus \{0\})$ is a bounded set.

Let me use the standard area theorem proof. Consider the function $\phi(w) = 1/(h(1/w) - \text{something})$... Actually, let me use the direct approach from the hint.

**Direct computation of area of complement:**

For $0 < \rho < 1$, consider the image of the circle $|z| = \rho$ under $h$. This gives a Jordan curve $\Gamma_\rho$. The interior of $\Gamma_\rho$ (for small $\rho$) is the complement of $h(D_\rho \setminus \{0\})$ (more precisely, the bounded component of the complement).

The area enclosed by $\Gamma_\rho$ can be computed using Green's theorem:
$$\text{Area} = \frac{1}{2i} \oint_{|z|=\rho} \overline{h(z)} h'(z) \, dz$$

Wait, let me be more careful. The area of the complement of $h(D_\rho \setminus \{0\})$ is:

Since $h(z) = 1/z + c_0 + c_1 z + \cdots$, as $z \to 0$, $h(z) \to \infty$. So $h(D_\rho \setminus \{0\})$ is an unbounded domain, and its complement is bounded.

The area of the complement is:
$$A = \pi \cdot \frac{1}{\rho^2} - \pi \sum_{n=1}^{\infty} n |c_n|^2 \rho^{2n}$$

Wait, let me derive this properly.

Consider the inverse function $g = h^{-1}$ defined on the complement of $h(D_\rho \setminus \{0\})$. Near infinity, $g(w) \sim 1/w$.

Actually, let me use the standard approach. The area of the complement of $h(D_\rho \setminus \{0\})$ can be computed as follows.

On $|z| = \rho$, parametrize $z = \rho e^{i\theta}$. Then $h(z) = \frac{1}{\rho} e^{-i\theta} + c_0 + c_1 \rho e^{i\theta} + c_2 \rho^2 e^{2i\theta} + \cdots$

The area enclosed by the curve $w(\theta) = h(\rho e^{i\theta})$ (which bounds the complement) is:

$$A = \frac{1}{2i} \int_0^{2\pi} \overline{w(\theta)} w'(\theta) \, d\theta$$

where $w(\theta) = h(\rho e^{i\theta})$ and $w'(\theta) = i\rho e^{i\theta} h'(\rho e^{i\theta})$.

So:
$$A = \frac{1}{2i} \int_0^{2\pi} \overline{h(\rho e^{i\theta})} \cdot i\rho e^{i\theta} h'(\rho e^{i\theta}) \, d\theta = \frac{\rho}{2} \int_0^{2\pi} \overline{h(\rho e^{i\theta})} h'(\rho e^{i\theta}) e^{i\theta} \, d\theta$$

Hmm, this is getting complicated. Let me use a cleaner approach.

**Cleaner approach using the area formula:**

For an injective analytic function $h(z) = 1/z + \sum_{n=0}^{\infty} c_n z^n$ on $|z| < \rho$, the area of the complement of $h(D_\rho \setminus \{0\})$ is:

We use the fact that for a univalent function $g(w) = w + b_0 + b_1/w + \cdots$ defined near infinity, the area of the complement of $g$'s image is $\pi \sum_{n=1}^{\infty} n |b_n|^2$.

Let $w = 1/z$, so $z = 1/w$. When $|z| < \rho$, we have $|w| > 1/\rho$. Define:
$$G(w) = h(1/w) = w + c_0 + c_1/w + c_2/w^2 + \cdots$$

This is defined for $|w| > 1/\rho$ and is injective. $G(w) \to \infty$ as $w \to \infty$.

The image $G(\{|w| > 1/\rho\})$ equals $h(D_\rho \setminus \{0\})$.

The complement of $G(\{|w| > 1/\rho\})$ in $\mathbb{C}$ is a bounded set. Let's call it $K$.

Now, $G(w) = w + c_0 + c_1/w + c_2/w^2 + \cdots$ for $|w| > 1/\rho$.

The area of the complement of the image of $\{|w| = R\}$ (for $R > 1/\rho$) under $G$ is:

Using the area theorem for functions of the form $G(w) = w + c_0 + c_1/w + c_2/w^2 + \cdots$ on $|w| = R$:

The area enclosed by $G(|w| = R)$ (the image curve) is:
$$\text{Area enclosed} = \pi R^2 - \pi \sum_{n=1}^{\infty} n |c_n|^2 R^{-2n}$$

Wait, let me be more precise. For $G(w) = w + \sum_{n=0}^{\infty} c_n w^{-n}$ on $|w| = R$:

$$\frac{1}{2i} \oint_{|w|=R} \overline{G(w)} G'(w) \, dw$$

$G'(w) = 1 - c_1/w^2 - 2c_2/w^3 - \cdots$

$\overline{G(w)} = \overline{w} + \overline{c_0} + \overline{c_1} \overline{w}^{-1} + \cdots$

On $|w| = R$: $\overline{w} = R^2/w$, so $\overline{G(w)} = R^2/w + \overline{c_0} + \overline{c_1} R^2/w + \cdots$

Hmm, this is getting messy. Let me use the standard result directly.

**Standard Area Theorem:** For $G(w) = w + b_0 + b_1/w + b_2/w^2 + \cdots$ univalent in $|w| > R_0$, the area of the complement of $G(\{|w| > R_0\})$ is:
$$\pi \sum_{n=1}^{\infty} n |b_n|^2 R_0^{-2n}$$

Wait no. Let me think again.

Actually, the standard result is: if $G(w) = w + b_0 + b_1/w + b_2/w^2 + \cdots$ is univalent in $|w| > 1$ (say), then $\sum_{n=1}^{\infty} n|b_n|^2 \leq 1$.

The proof goes: the area of the complement of $G(\{|w| > 1\})$ equals $\pi(1 - \sum_{n=1}^{\infty} n|b_n|^2) \geq 0$, hence $\sum n|b_n|^2 \leq 1$.

Let me derive this. On $|w| = R$ (large), $G(w) = w + b_0 + b_1/w + \cdots$. The area enclosed by the image curve $G(Re^{i\theta})$, $\theta \in [0, 2\pi]$, is:

$$A(R) = \frac{1}{2i} \int_0^{2\pi} \overline{G(Re^{i\theta})} G'(Re^{i\theta}) \cdot iRe^{i\theta} \, d\theta$$

Wait, more carefully: if $\gamma(t) = G(Re^{it})$ for $t \in [0, 2\pi]$, then the signed area enclosed is:
$$A = \frac{1}{2i} \oint_\gamma \bar{w} \, dw = \frac{1}{2i} \int_0^{2\pi} \overline{G(Re^{it})} G'(Re^{it}) iRe^{it} \, dt$$

Let me write $w = Re^{it}$, $dw = iRe^{it} dt$.

$$A = \frac{1}{2i} \int_0^{2\pi} \overline{G(w)} G'(w) \, dw$$

where the integral is over $|w| = R$.

$G(w) = w + b_0 + b_1/w + b_2/w^2 + \cdots$
$G'(w) = 1 - b_1/w^2 - 2b_2/w^3 - \cdots$

On $|w| = R$: $\bar{w} = R^2/w$.

$\overline{G(w)} = \bar{w} + \bar{b_0} + \bar{b_1}/\bar{w} + \bar{b_2}/\bar{w}^2 + \cdots = R^2/w + \bar{b_0} + \bar{b_1}R^2/w + \bar{b_2}R^4/w^2 + \cdots$

Wait, $\bar{w} = R^2/w$ on $|w| = R$. And $\bar{b_n}/\bar{w}^n = \bar{b_n} \cdot w^n / R^{2n}$.

So $\overline{G(w)} = R^2/w + \bar{b_0} + \bar{b_1}w/R^2 + \bar{b_2}w^2/R^4 + \cdots$

Now:
$$\overline{G(w)} G'(w) = \left(\frac{R^2}{w} + \bar{b_0} + \frac{\bar{b_1}w}{R^2} + \frac{\bar{b_2}w^2}{R^4} + \cdots\right)\left(1 - \frac{b_1}{w^2} - \frac{2b_2}{w^3} - \cdots\right)$$

We need $\frac{1}{2i}\oint_{|w|=R} \overline{G(w)} G'(w) dw$. Only the residue (coefficient of $1/w$) in the Laurent expansion of $\overline{G(w)} G'(w)$ contributes.

The coefficient of $1/w$ in $\overline{G(w)} G'(w)$:

From $R^2/w \cdot 1$: gives $R^2/w$. Coefficient of $1/w$: $R^2$.

From $\bar{b_0} \cdot (-b_1/w^2)$: gives $-\bar{b_0}b_1/w^2$. Not $1/w$.

From $\bar{b_1}w/R^2 \cdot (-b_1/w^2) = -\bar{b_1}b_1/(R^2 w)$: Coefficient of $1/w$: $-|b_1|^2/R^2$.

From $\bar{b_2}w^2/R^4 \cdot (-2b_2/w^3) = -2\bar{b_2}b_2/(R^4 w) = -2|b_2|^2/R^4$: Coefficient of $1/w$: $-2|b_2|^2/R^4$.

In general, from $\bar{b_n}w^n/R^{2n} \cdot (-nb_n/w^{n+1}) = -n|b_n|^2/(R^{2n}w)$: Coefficient of $1/w$: $-n|b_n|^2/R^{2n}$.

So the residue at $\infty$ (or rather, the coefficient of $1/w$) is:
$$R^2 - \sum_{n=1}^{\infty} \frac{n|b_n|^2}{R^{2n}}$$

Therefore:
$$A(R) = \frac{1}{2i} \cdot 2\pi i \left(R^2 - \sum_{n=1}^{\infty} \frac{n|b_n|^2}{R^{2n}}\right) = \pi\left(R^2 - \sum_{n=1}^{\infty} \frac{n|b_n|^2}{R^{2n}}\right)$$

This is the signed area enclosed by the image curve $G(|w| = R)$. Since $G$ is injective, this equals the area of the region enclosed.

Now, for our situation: $G(w) = h(1/w) = w + c_0 + c_1/w + c_2/w^2 + \cdots$ defined for $|w| > 1/\rho$.

The image $G(\{|w| > 1/\rho\}) = h(D_\rho \setminus \{0\})$.

The complement of this image is a bounded set. As $R \to 1/\rho$ from above, the image curve $G(|w| = R)$ approaches the boundary of the image of $|z| = \rho$ under $h$.

Actually, let me reconsider. The area of the complement of $h(D_\rho \setminus \{0\})$ is what we want.

$G$ maps $\{|w| > 1/\rho\}$ to some domain. The complement of this domain is bounded. The area of the complement is:

As $R \to \infty$, $A(R) \to \infty$ (it's approximately $\pi R^2$). The area enclosed by $G(|w| = R)$ is the area of the image of $\{|w| < R\}$ under $G$... no wait, it's the area enclosed by the curve $G(|w| = R)$.

Hmm, let me think about this differently. $G$ maps $\{|w| > 1/\rho\}$ conformally onto some domain $\Omega$. The complement $\mathbb{C} \setminus \Omega$ is compact. The area of $\mathbb{C} \setminus \Omega$ is what we want.

The curve $G(|w| = R)$ for $R > 1/\rho$ lies in $\Omega$ and encloses a region that contains $\mathbb{C} \setminus \Omega$ in its interior (for large enough $R$... actually for any $R > 1/\rho$ since $G$ is injective).

Wait, actually: $G(|w| = R)$ for $R > 1/\rho$ is a Jordan curve. The interior of this curve contains $\mathbb{C} \setminus G(\{|w| > R\})$... hmm no.

Let me think again. $G$ maps $\{|w| > 1/\rho\}$ injectively to $\Omega$. As $|w| \to \infty$, $G(w) \to \infty$. So $\Omega$ is an unbounded domain. Its complement $K = \mathbb{C} \setminus \Omega$ is compact.

For $R > 1/\rho$, the curve $\Gamma_R = G(|w| = R)$ lies in $\Omega$. The interior of $\Gamma_R$ contains $K$ (since $K$ is bounded and lies in the complement of $G(\{|w| > R\})$, and by continuity/jordan curve theorem).

The area enclosed by $\Gamma_R$ equals:
- Area of $K$ + Area of $G(\{1/\rho < |w| < R\})$

So: $A(R) = \text{Area}(K) + \text{Area}(G(\{1/\rho < |w| < R\}))$

And $\text{Area}(G(\{1/\rho < |w| < R\})) = \int_{1/\rho}^{R} \int_0^{2\pi} |G'(Re^{i\theta})|^2 R \, dR \, d\theta$... no, that's not right either.

Actually: $\text{Area}(G(\{1/\rho < |w| < R\})) = \int_{1/\rho < |w| < R} |G'(w)|^2 \, dx \, dy$

where $w = x + iy$. In polar coordinates:
$$= \int_{1/\rho}^{R} \int_0^{2\pi} |G'(re^{i\theta})|^2 r \, d\theta \, dr$$

But also, the signed area formula gives:
$$A(R) = \pi\left(R^2 - \sum_{n=1}^{\infty} \frac{n|b_n|^2}{R^{2n}}\right)$$

where $b_n = c_n$ in our case.

And $A(R) = \text{Area}(K) + \text{Area}(G(\{1/\rho < |w| < R\}))$.

As $R \to 1/\rho^+$, $A(R) \to \text{Area}(K)$ (since the annular area goes to 0).

So: $\text{Area}(K) = \lim_{R \to (1/\rho)^+} \pi\left(R^2 - \sum_{n=1}^{\infty} \frac{n|c_n|^2}{R^{2n}}\right) = \pi\left(\frac{1}{\rho^2} - \sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n}\right)$

Since Area$(K) \geq 0$:
$$\frac{1}{\rho^2} - \sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n} \geq 0$$
$$\sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n} \leq \frac{1}{\rho^2}$$

Letting $\rho \to 1^-$:
$$\sum_{n=1}^{\infty} n|c_n|^2 \leq 1$$

This proves part (c).

## Part (d): Existence of $g$ with $g^2(z) = f(z^2)$

Given $f(z) = z + a_2 z^2 + a_3 z^3 + \cdots$ is injective on $\mathbb{D}$, $f(0) = 0$, $f'(0) = 1$.

**Step 1:** $f(z)/z = 1 + a_2 z + a_3 z^2 + \cdots$ is holomorphic on $\mathbb{D}$.

We need to show $f(z)/z \neq 0$ on $\mathbb{D}$. Since $f(0) = 0$ and $f'(0) = 1 \neq 0$, by continuity $f(z)/z \neq 0$ near 0. For $z \neq 0$, if $f(z)/z = 0$ then $f(z) = 0 = f(0)$, contradicting injectivity. So $f(z)/z \neq 0$ on all of $\mathbb{D}$.

**Step 2:** Since $\mathbb{D}$ is simply connected and $f(z)/z$ is holomorphic and nowhere vanishing, there exists a holomorphic square root $\psi(z)$ with $\psi(z)^2 = f(z)/z$ and $\psi(0) = 1$ (choosing the branch with $\psi(0) = 1$ since $f(0)/0 = 1$ in the limit).

**Step 3:** Define $g(z) = z\psi(z^2)$. Then:
$$g(z)^2 = z^2 \psi(z^2)^2 = z^2 \cdot \frac{f(z^2)}{z^2} = f(z^2)$$

**Step 4:** $g(0) = 0$ and $g'(0) = \psi(0) = 1$.

**Step 5:** $g$ is injective. Suppose $g(z_1) = g(z_2)$. Then $g(z_1)^2 = g(z_2)^2$, so $f(z_1^2) = f(z_2^2)$. Since $f$ is injective, $z_1^2 = z_2^2$, so $z_1 = \pm z_2$.

If $z_1 = -z_2 \neq 0$, then $g(z_1) = g(-z_1)$, so $z_1 \psi(z_1^2) = -z_1 \psi(z_1^2)$, which gives $2z_1\psi(z_1^2) = 0$. Since $z_1 \neq 0$ and $\psi(z_1^2) \neq 0$ (because $\psi^2(z_1^2) = f(z_1^2)/z_1^2 \neq 0$ as $f(z_1^2) \neq 0$ for $z_1^2 \neq 0$), this is a contradiction. So $z_1 = z_2$.

Wait, I need to be more careful. $\psi(z_1^2) \neq 0$ because $\psi^2(z_1^2) = f(z_1^2)/z_1^2$ and $f(z_1^2) \neq 0$ (since $f$ is injective and $f(0) = 0$, and $z_1^2 \neq 0$). So indeed $\psi(z_1^2) \neq 0$, contradiction.

Also, $g$ is odd: $g(-z) = -z\psi((-z)^2) = -z\psi(z^2) = -g(z)$.

## Part (e): $|a_2| \leq 2$ with equality characterization

**Step 1:** Since $g$ is injective with $g(0) = 0$, $g'(0) = 1$, and $g$ is odd (as shown above), $g(z) = z + b_3 z^3 + b_5 z^5 + \cdots$ (only odd powers).

From $g(z) = z\psi(z^2)$ and $\psi(z) = 1 + \frac{a_2}{2}z + \frac{a_3}{2}z^2 + \cdots$ (since $\psi^2(z) = f(z)/z = 1 + a_2 z + a_3 z^2 + \cdots$, and $\psi(z) = 1 + \frac{a_2}{2}z + \cdots$ by expanding the square root):

Actually, let me compute $\psi$ more carefully. $\psi(z)^2 = 1 + a_2 z + a_3 z^2 + \cdots$. Writing $\psi(z) = 1 + \alpha_1 z + \alpha_2 z^2 + \cdots$:
$(1 + \alpha_1 z + \alpha_2 z^2 + \cdots)^2 = 1 + 2\alpha_1 z + (\alpha_1^2 + 2\alpha_2)z^2 + \cdots$

So $2\alpha_1 = a_2$, giving $\alpha_1 = a_2/2$.

Then $g(z) = z\psi(z^2) = z(1 + \frac{a_2}{2}z^2 + \cdots) = z + \frac{a_2}{2}z^3 + \cdots$

So $g(z) = z + b_3 z^3 + \cdots$ where $b_3 = a_2/2$.

**Step 2:** Consider $1/g(z)$. Since $g$ has a simple zero at 0, $1/g$ has a simple pole at 0:
$$1/g(z) = \frac{1}{z} + d_0 + d_1 z + d_2 z^2 + \cdots$$

Since $g(z) = z + b_3 z^3 + \cdots$:
$$\frac{1}{g(z)} = \frac{1}{z(1 + b_3 z^2 + \cdots)} = \frac{1}{z}(1 - b_3 z^2 + \cdots) = \frac{1}{z} - b_3 z + \cdots$$

So $d_1 = -b_3 = -a_2/2$.

**Step 3:** $1/g(z)$ is injective on $\mathbb{D}$ (since $g$ is injective and $1/w$ is injective on $\mathbb{C} \setminus \{0\}$, and $g$ maps $\mathbb{D}$ to a set not containing 0... wait, $g(0) = 0$. Let me reconsider.

Actually, $1/g(z)$ is defined on $\mathbb{D} \setminus \{0\}$ and is injective there. It has a simple pole at 0. So it's injective and meromorphic on $\mathbb{D}$ with a pole at 0.

To apply part (c), we need $h$ to be injective on $0 < |z| < 1$. Indeed, $1/g(z)$ is injective on $\mathbb{D} \setminus \{0\}$ (since $g$ is injective and nonzero on $\mathbb{D} \setminus \{0\}$, and $w \mapsto 1/w$ is injective on $\mathbb{C} \setminus \{0\}$).

So by part (c) applied to $h(z) = 1/g(z) = 1/z + d_0 + d_1 z + \cdots$:
$$\sum_{n=1}^{\infty} n|d_n|^2 \leq 1$$

In particular, $|d_1|^2 \leq 1$, so $|d_1| \leq 1$.

Since $d_1 = -a_2/2$, we get $|a_2/2| \leq 1$, i.e., $|a_2| \leq 2$.

**Step 4: Equality case.** $|a_2| = 2$ iff $|d_1| = 1$ iff equality holds in $\sum n|d_n|^2 \leq 1$, which means $d_n = 0$ for all $n \geq 2$ (and $|d_1| = 1$).

So $1/g(z) = 1/z + d_1 z$ with $|d_1| = 1$. Write $d_1 = e^{i\theta}$.

Then $1/g(z) = 1/z + e^{i\theta}z$, so:
$$g(z) = \frac{1}{1/z + e^{i\theta}z} = \frac{z}{1 + e^{i\theta}z^2}$$

Then $f(z^2) = g(z)^2 = \frac{z^2}{(1 + e^{i\theta}z^2)^2}$.

Substituting $w = z^2$: $f(w) = \frac{w}{(1 + e^{i\theta}w)^2}$.

So $f(z) = \frac{z}{(1 + e^{i\theta}z)^2}$.

Writing $e^{i\theta} = -e^{i\alpha}$ (i.e., replacing $\theta$ by $\alpha + \pi$): $f(z) = \frac{z}{(1 - e^{i\alpha}z)^2}$.

This is the Koebe function (up to rotation). So equality holds iff $f(z) = \frac{z}{(1 - e^{i\theta}z)^2}$ for some $\theta$.

## Part (f): $|z_1 - z_2| \leq 4$

Let $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \cdots$ be injective on $\mathbb{D}$ and avoid values $z_1$ and $z_2$.

Consider $\phi_j(z) = 1/(h(z) - z_j)$ for $j = 1, 2$.

Since $h$ avoids $z_j$, $h(z) - z_j \neq 0$ for all $z \in \mathbb{D}$. Also, $h(z) - z_j$ has a simple pole at $z = 0$ (since $h$ has a simple pole at 0). So $\phi_j(z) = 1/(h(z) - z_j)$ is holomorphic on $\mathbb{D}$ (the pole of $h$ at 0 becomes a zero of $h(z) - z_j$ at 0, and taking the reciprocal makes it a... wait.

Let me reconsider. $h(z) = 1/z + c_0 + c_1 z + \cdots$ on $0 < |z| < 1$. Then $h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + \cdots$, which has a simple pole at $z = 0$.

So $1/(h(z) - z_j) = \frac{1}{1/z + (c_0 - z_j) + c_1 z + \cdots} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$

This is holomorphic near 0 (the singularity at 0 is removable, and the function vanishes at 0).

$\phi_j(z) = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots} = z - (c_0 - z_j)z^2 + \cdots$

So $\phi_j(0) = 0$ and $\phi_j'(0) = 1$.

Now, is $\phi_j$ injective? Since $h$ is injective and $w \mapsto 1/(w - z_j)$ is injective on $\mathbb{C} \setminus \{z_j\}$ (and $h$ avoids $z_j$), the composition $\phi_j = 1/(h - z_j)$ is injective on $\mathbb{D} \setminus \{0\}$. And $\phi_j$ extends holomorphically to 0 with $\phi_j(0) = 0$.

Actually, we need to check that $\phi_j$ is injective on all of $\mathbb{D}$. Since $h$ is injective on $0 < |z| < 1$ and $\phi_j$ is the composition of $h$ with the injective map $w \mapsto 1/(w - z_j)$ (on the range of $h$, which avoids $z_j$), $\phi_j$ is injective on $\mathbb{D} \setminus \{0\}$. At $z = 0$: $\phi_j(0) = 0$, and for $z \neq 0$, $\phi_j(z) = 1/(h(z) - z_j) \neq 0$ (since $h(z) - z_j \neq \infty$ for $z \neq 0$... well, $h(z)$ is finite for $z \neq 0$, so $\phi_j(z)$ is finite and nonzero iff $h(z) \neq \infty$, which is true for $z \neq 0$). Wait, $\phi_j(z) = 0$ iff $h(z) = \infty$, which only happens at $z = 0$. So $\phi_j(z) \neq 0 = \phi_j(0)$ for $z \neq 0$. Thus $\phi_j$ is injective on $\mathbb{D}$.

So $\phi_j: \mathbb{D} \to \mathbb{C}$ is holomorphic, injective, $\phi_j(0) = 0$, $\phi_j'(0) = 1$.

Write $\phi_j(z) = z + \beta_{j,2} z^2 + \cdots$. From the expansion above: $\beta_{j,2} = -(c_0 - z_j) = z_j - c_0$.

By part (e), $|\beta_{j,2}| \leq 2$, so $|z_j - c_0| \leq 2$ for $j = 1, 2$.

Therefore: $|z_1 - z_2| = |(z_1 - c_0) - (z_2 - c_0)| \leq |z_1 - c_0| + |z_2 - c_0| \leq 2 + 2 = 4$.

## Part (g): Completing the proof

**Theorem:** If $f: \mathbb{D} \to \mathbb{C}$ is injective, holomorphic, with $f(0) = 0$ and $f'(0) = 1$, then $D_{1/4}(0) \subseteq f(\mathbb{D})$.

**Proof:** Suppose for contradiction that there exists $w \in \mathbb{C}$ with $|w| < 1/4$ such that $w \notin f(\mathbb{D})$.

Since $f$ is injective and $f(0) = 0$, we have $f(z) \neq 0$ for all $z \neq 0$ in $\mathbb{D}$. So $0 \notin f(\mathbb{D} \setminus \{0\})$.

Consider $h(z) = 1/f(z)$, defined on $\mathbb{D} \setminus \{0\}$. Then:
- $h$ has a simple pole at $z = 0$ (since $f$ has a simple zero at 0).
- $h$ is injective on $\mathbb{D} \setminus \{0\}$ (since $f$ is injective and $w \mapsto 1/w$ is injective on $\mathbb{C} \setminus \{0\}$).
- $h$ avoids the value $0$ (since $f$ is finite, $1/f$ is never $\infty$... wait, $h(z) = 0$ would mean $f(z) = \infty$, which doesn't happen). Actually $h$ avoids $0$ because $f(z)$ is always finite.
- $h$ avoids $1/w$ because $f$ avoids $w$.

So $h(z) = 1/f(z)$ is injective on $0 < |z| < 1$ and avoids the values $0$ and $1/w$.

By part (f): $|0 - 1/w| \leq 4$, i.e., $1/|w| \leq 4$, i.e., $|w| \geq 1/4$.

This contradicts $|w| < 1/4$. Therefore $D_{1/4}(0) \subseteq f(\mathbb{D})$.

**Sharpness:** The Koebe function $f(z) = z/(1-z)^2 = z + 2z^2 + 3z^3 + \cdots$ satisfies $f(0) = 0$, $f'(0) = 1$, is injective on $\mathbb{D}$, and its image is $\mathbb{C} \setminus (-\infty, -1/4]$. So $-1/4 \notin f(\mathbb{D})$, showing that $r = 1/4$ is optimal.

Wait, let me double-check part (f) more carefully. The hint says "Look at the second coefficient in the power series expansion of $1/(h(z) - z_j)$."

So in part (f), $h(z) = 1/z + c_0 + c_1 z + \cdots$ is injective on $\mathbb{D}$ (the problem says "injective on $\mathbb{D}$" but I think it means on $0 < |z| < 1$ since $h$ has a pole at 0).

Actually, re-reading part (f): "If $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \cdots$ is injective on $\mathbb{D}$ and avoids the values $z_1$ and $z_2$..."

I think this means $h$ is defined and injective on $\mathbb{D} \setminus \{0\}$ (or perhaps on the punctured disk $0 < |z| < 1$).

The function $\phi_j(z) = 1/(h(z) - z_j)$:
- At $z = 0$: $h(z) - z_j = 1/z + (c_0 - z_j) + \cdots$, so $\phi_j(z) = z/(1 + (c_0 - z_j)z + \cdots) = z - (c_0 - z_j)z^2 + \cdots$
- $\phi_j(0) = 0$, $\phi_j'(0) = 1$.

By part (e), the second coefficient of $\phi_j$ satisfies $|\beta_{j,2}| \leq 2$.

$\beta_{j,2} = -(c_0 - z_j) = z_j - c_0$.

So $|z_1 - c_0| \leq 2$ and $|z_2 - c_0| \leq 2$.

By triangle inequality: $|z_1 - z_2| \leq |z_1 - c_0| + |c_0 - z_2| \leq 4$. ✓

Now let me also verify the injectivity argument for $\phi_j$ more carefully.

$h: \mathbb{D} \setminus \{0\} \to \mathbb{C}$ is injective and avoids $z_j$. The map $w \mapsto 1/(w - z_j)$ is injective on $\mathbb{C} \setminus \{z_j\}$ (it's a Möbius transformation). Since $h(\mathbb{D} \setminus \{0\}) \subset \mathbb{C} \setminus \{z_j\}$, the composition $\phi_j = 1/(h - z_j)$ is injective on $\mathbb{D} \setminus \{0\}$.

Now, $\phi_j$ extends to $z = 0$ with $\phi_j(0) = 0$. For $z \neq 0$, $\phi_j(z) = 1/(h(z) - z_j)$ is finite (since $h(z)$ is finite for $z \neq 0$) and nonzero (since $h(z) \neq \infty$ for $z \neq 0$, and $h(z) - z_j \neq 0$ since $h$ avoids $z_j$). So $\phi_j(z) \neq 0 = \phi_j(0)$ for $z \neq 0$. Thus $\phi_j$ is injective on all of $\mathbb{D}$. ✓

And $\phi_j$ satisfies $\phi_j(0) = 0$, $\phi_j'(0) = 1$, and is injective. So part (e) applies. ✓

Let me now write up the complete solution more carefully.

Actually, let me reconsider part (c) more carefully. The hint says "Calculate the area of the complement of $h(D_\rho(0) - \{0\})$ where $0 < \rho < 1$, and let $\rho \to 1$."

So we need to compute the area of the complement of $h(\{0 < |z| < \rho\})$ for $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \cdots$ injective on $0 < |z| < 1$.

$h$ maps the punctured disk $D_\rho(0) \setminus \{0\}$ to some domain. Since $h(z) \to \infty$ as $z \to 0$, the image is unbounded, and its complement in $\mathbb{C}$ is a compact set (let's call it $K_\rho$).

To compute the area of $K_\rho$, we use the substitution $w = 1/z$. Let $G(w) = h(1/w) = w + c_0 + c_1/w + c_2/w^2 + \cdots$. This is defined for $|w| > 1/\rho$.

$G$ maps $\{|w| > 1/\rho\}$ to the same image as $h$ maps $\{0 < |z| < \rho\}$, i.e., $G(\{|w| > 1/\rho\}) = h(D_\rho(0) \setminus \{0\})$.

The complement of this image is $K_\rho$.

Now, for $R > 1/\rho$, the image of the circle $|w| = R$ under $G$ is a Jordan curve $\Gamma_R$. The area enclosed by $\Gamma_R$ equals:

$$\text{Area enclosed by } \Gamma_R = \pi\left(R^2 - \sum_{n=1}^{\infty} n|c_n|^2 R^{-2n}\right)$$

(This is the standard formula derived above.)

This enclosed area = Area$(K_\rho)$ + Area$(G(\{1/\rho < |w| < R\}))$.

As $R \to (1/\rho)^+$:
- Area enclosed by $\Gamma_R \to$ Area$(K_\rho)$ (since the annular region shrinks to zero)
- $\pi\left(R^2 - \sum_{n=1}^{\infty} n|c_n|^2 R^{-2n}\right) \to \pi\left(1/\rho^2 - \sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n}\right)$

So Area$(K_\rho) = \pi\left(1/\rho^2 - \sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n}\right) \geq 0$.

This gives $\sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n} \leq 1/\rho^2$.

As $\rho \to 1^-$: $\sum_{n=1}^{\infty} n|c_n|^2 \leq 1$. ✓

Now let me also think about whether the formula for the area enclosed by $\Gamma_R$ needs more justification.

The signed area enclosed by a Jordan curve $\gamma(t) = G(Re^{it})$, $t \in [0, 2\pi]$, is:
$$A = \frac{1}{2i} \oint_{\Gamma_R} \bar{w} \, dw = \frac{1}{2i} \int_0^{2\pi} \overline{G(Re^{it})} G'(Re^{it}) iRe^{it} \, dt$$

$= \frac{1}{2} \int_0^{2\pi} \overline{G(Re^{it})} G'(Re^{it}) Re^{it} \, dt$

Hmm, let me use the complex integral form. For a curve $\gamma(t) = x(t) + iy(t)$:
$$\text{Area} = \frac{1}{2} \int_0^{2\pi} (x\dot{y} - y\dot{x}) \, dt = \frac{1}{2i} \int_0^{2\pi} \bar{\gamma} \dot{\gamma} \, dt$$

With $\gamma(t) = G(Re^{it})$, $\dot{\gamma}(t) = G'(Re^{it}) \cdot iRe^{it}$.

$$\text{Area} = \frac{1}{2i} \int_0^{2\pi} \overline{G(Re^{it})} G'(Re^{it}) iRe^{it} \, dt = \frac{R}{2} \int_0^{2\pi} \overline{G(Re^{it})} G'(Re^{it}) e^{it} \, dt$$

Alternatively, using complex variable notation with $w = Re^{it}$:
$$\text{Area} = \frac{1}{2i} \oint_{|w|=R} \overline{G(w)} G'(w) \, dw$$

Wait, $dw = iRe^{it} dt$, so $dt = dw/(iRe^{it}) = dw/(iw)$. And:
$$\text{Area} = \frac{1}{2i} \int \overline{G(w)} G'(w) \cdot \frac{dw}{iw} \cdot iw$$

Hmm, let me just do it directly.

$$\text{Area} = \frac{1}{2i} \oint_{|w|=R} \overline{G(w)} G'(w) \, dw$$

Wait no. Let me redo this. The area formula for a parametrized curve $\gamma(t) = G(R e^{it})$, $t \in [0, 2\pi]$:

$$A = \frac{1}{2i} \int_0^{2\pi} \overline{\gamma(t)} \gamma'(t) \, dt$$

$\gamma'(t) = G'(Re^{it}) \cdot iRe^{it}$

$A = \frac{1}{2i} \int_0^{2\pi} \overline{G(Re^{it})} G'(Re^{it}) iRe^{it} \, dt$

Now substitute $w = Re^{it}$, $dw = iRe^{it} dt$, so $dt = dw/(iRe^{it}) = dw/(iw)$:

$A = \frac{1}{2i} \oint_{|w|=R} \overline{G(w)} G'(w) \frac{dw}{iw} \cdot iw$

Hmm, this isn't simplifying nicely. Let me just compute directly.

$A = \frac{1}{2i} \int_0^{2\pi} \overline{G(Re^{it})} G'(Re^{it}) iRe^{it} \, dt$

$= \frac{R}{2} \int_0^{2\pi} \overline{G(Re^{it})} G'(Re^{it}) e^{it} \, dt$

Let me write $G(w) = \sum_{n=-\infty}^{\infty} a_n w^n$ where $a_1 = 1$, $a_0 = c_0$, $a_{-n} = c_n$ for $n \geq 1$.

On $|w| = R$: $\bar{w} = R^2/w$, so $\bar{w}^n = R^{2n}/w^n$.

$\overline{G(w)} = \sum_n \bar{a}_n \bar{w}^n = \sum_n \bar{a}_n R^{2n}/w^n$

$G'(w) = \sum_n n a_n w^{n-1}$

$\overline{G(w)} G'(w) = \left(\sum_n \bar{a}_n R^{2n} w^{-n}\right) \left(\sum_m m a_m w^{m-1}\right)$

The integral $\frac{R}{2} \int_0^{2\pi} \overline{G(Re^{it})} G'(Re^{it}) e^{it} \, dt$ with $w = Re^{it}$, $e^{it} = w/R$:

$= \frac{R}{2} \int_0^{2\pi} \overline{G(w)} G'(w) \frac{w}{R} \, dt = \frac{1}{2} \int_0^{2\pi} \overline{G(w)} G'(w) w \, dt$

$= \frac{1}{2} \oint_{|w|=R} \overline{G(w)} G'(w) w \frac{dw}{iw}$

$= \frac{1}{2i} \oint_{|w|=R} \overline{G(w)} G'(w) \, dw$

OK so the area is:
$$A = \frac{1}{2i} \oint_{|w|=R} \overline{G(w)} G'(w) \, dw$$

Now, $\overline{G(w)} G'(w) = \left(\sum_n \bar{a}_n R^{2n} w^{-n}\right)\left(\sum_m m a_m w^{m-1}\right)$

The integral picks out the coefficient of $w^{-1}$ (residue theorem: $\oint w^k dw = 2\pi i$ if $k = -1$, else 0).

We need $-n + m - 1 = -1$, i.e., $m = n$.

Coefficient of $w^{-1}$: $\sum_n \bar{a}_n R^{2n} \cdot n a_n = \sum_n n |a_n|^2 R^{2n}$

So: $A = \frac{1}{2i} \cdot 2\pi i \sum_n n|a_n|^2 R^{2n} = \pi \sum_n n|a_n|^2 R^{2n}$

But wait, we need to be careful about which $n$ contribute. $a_n$ for our function $G$:
- $a_1 = 1$ (coefficient of $w$)
- $a_0 = c_0$ (constant term)
- $a_{-n} = c_n$ for $n \geq 1$ (coefficient of $w^{-n}$)

So $\sum_n n|a_n|^2 R^{2n} = 1 \cdot |a_1|^2 R^2 + 0 \cdot |a_0|^2 + \sum_{n \geq 1} (-n)|a_{-n}|^2 R^{-2n}$

Wait, $n$ ranges over all integers. For $n \geq 2$: $|a_n|^2 R^{2n}$ with $a_n$ being the coefficient of $w^n$ (which is 0 for $n \geq 2$ in our case). For $n = 1$: $|a_1|^2 R^2 = R^2$. For $n = 0$: contributes 0. For $n \leq -1$: $n|a_n|^2 R^{2n}$ with $a_n = c_{-n}$ for $n = -1, -2, \ldots$

So $\sum_{n=-\infty}^{\infty} n|a_n|^2 R^{2n} = R^2 + \sum_{n=1}^{\infty} (-n)|c_n|^2 R^{-2n} = R^2 - \sum_{n=1}^{\infty} n|c_n|^2 R^{-2n}$

Therefore: $A(R) = \pi(R^2 - \sum_{n=1}^{\infty} n|c_n|^2 R^{-2n})$

This is the area enclosed by $\Gamma_R = G(|w| = R)$.

Now, as I argued before, this equals Area$(K_\rho)$ + Area$(G(\{1/\rho < |w| < R\}))$.

As $R \to (1/\rho)^+$: $A(R) \to \pi(1/\rho^2 - \sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n})$.

And Area$(G(\{1/\rho < |w| < R\})) \to 0$.

So Area$(K_\rho) = \pi(1/\rho^2 - \sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n}) \geq 0$.

Hence $\sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n} \leq 1/\rho^2$.

As $\rho \to 1^-$: $\sum_{n=1}^{\infty} n|c_n|^2 \leq 1$. ✓

Great, this confirms part (c).

Now let me also verify part (f) more carefully.

In part (f), we have $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \cdots$ injective on $0 < |z| < 1$, avoiding values $z_1, z_2$.

For $j = 1, 2$, define $\phi_j(z) = 1/(h(z) - z_j)$ for $z \in \mathbb{D} \setminus \{0\}$.

$h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + \cdots$

$\phi_j(z) = \frac{1}{1/z + (c_0 - z_j) + c_1 z + \cdots} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$

So $\phi_j$ extends to $z = 0$ with $\phi_j(0) = 0$.

$\phi_j(z) = z \cdot \frac{1}{1 + (c_0 - z_j)z + \cdots} = z(1 - (c_0 - z_j)z + \cdots) = z - (c_0 - z_j)z^2 + \cdots$

So $\phi_j'(0) = 1$ and the coefficient of $z^2$ is $\beta_{j,2} = -(c_0 - z_j) = z_j - c_0$.

$\phi_j$ is injective on $\mathbb{D}$ (as argued above).

$\phi_j$ satisfies the hypotheses of the Koebe theorem (injective, $\phi_j(0) = 0$, $\phi_j'(0) = 1$).

By part (e), $|\beta_{j,2}| \leq 2$, i.e., $|z_j - c_0| \leq 2$ for $j = 1, 2$.

Therefore $|z_1 - z_2| \leq |z_1 - c_0| + |z_2 - c_0| \leq 2 + 2 = 4$. ✓

Now let me compile the full solution.

One thing I want to double-check: in part (e), when we say "by part (c) applied to $1/g$", we need $1/g$ to be injective on $0 < |z| < 1$. Since $g$ is injective on $\mathbb{D}$ with $g(0) = 0$, $g$ maps $\mathbb{D} \setminus \{0\}$ injectively to $\mathbb{C} \setminus \{0\}$ (well, to its image minus 0). And $1/w$ is injective on $\mathbb{C} \setminus \{0\}$. So $1/g$ is injective on $\mathbb{D} \setminus \{0\}$. ✓

Also, $1/g(z) = 1/z + d_0 + d_1 z + \cdots$ has the form required by part (c). ✓

Let me also make sure the equality case in part (e) is correct. If $|a_2| = 2$, then $|d_1| = 1$, and by equality in the area theorem (part c), all higher coefficients must be 0. So $1/g(z) = 1/z + d_1 z$ with $|d_1| = 1$. Write $d_1 = -e^{i\theta}$ (so that the final form matches). Then $1/g = 1/z - e^{i\theta} z$, so $g = z/(1 - e^{i\theta} z^2)$. Then $f(z^2) = g(z)^2 = z^2/(1 - e^{i\theta} z^2)^2$, so $f(z) = z/(1 - e^{i\theta} z)^2$. ✓

Actually, let me be more careful about the equality case in the area theorem. Part (c) says $\sum_{n=1}^{\infty} n|c_n|^2 \leq 1$. Equality holds iff the area of the complement is 0. For a function $h(z) = 1/z + c_0 + c_1 z + \cdots$ injective on the punctured disk, if the complement has area 0, then by the open mapping theorem, the image must be $\mathbb{C}$ minus a set of measure zero, which for a closed set means it's a single point or... Actually, the complement is compact, and if it has area 0, it must be a single point (or empty, but it can't be empty since $h$ maps to $\infty$ at $z = 0$).

Actually, the standard result is that equality in the area theorem forces $h(z) = 1/z + c_1 z$ with $|c_1| = 1$ (and $c_0 = 0$, $c_n = 0$ for $n \geq 2$). This is because the complement has area 0 and must be a point, and by the form of the Laurent expansion, this forces the specific form.

More precisely: if $\sum n|c_n|^2 = 1$, then Area$(K) = 0$. Since $K$ is compact and connected (for small perturbations), and $h$ maps a neighborhood of 0 (minus 0) to the complement of $K$, and $h(z) \sim 1/z$ near 0, the set $K$ must be a single point. If $K = \{p\}$, then $h$ maps $\mathbb{D} \setminus \{0\}$ to $\mathbb{C} \setminus \{p\}$, and $h(z) - p$ maps to $\mathbb{C} \setminus \{0\}$, so $1/(h(z) - p)$ maps to $\mathbb{C} \setminus \{0\}$... Actually this argument is getting circular. Let me just state the standard result.

The equality case in the area theorem: if $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \cdots$ is injective on $0 < |z| < 1$ and $\sum n|c_n|^2 = 1$, then $c_0 = 0$, $c_n = 0$ for $n \geq 2$, and $|c_1| = 1$. This is a standard result (see e.g., Duren's "Univalent Functions").

So $h(z) = 1/z + c_1 z$ with $|c_1| = 1$. In our application, $h = 1/g$, so $1/g(z) = 1/z + c_1 z$, giving $g(z) = z/(1 + c_1 z^2)$.

Then $f(z^2) = g(z)^2 = z^2/(1 + c_1 z^2)^2$, so $f(z) = z/(1 + c_1 z)^2$.

Writing $c_1 = -e^{i\theta}$: $f(z) = z/(1 - e^{i\theta} z)^2$. ✓

Now let me write the complete solution.

Actually, one more thing to verify in part (d): we need to show $g$ is injective. Let me redo this.

$g(z) = z\psi(z^2)$ where $\psi$ is holomorphic on $\mathbb{D}$ with $\psi^2 = f(\cdot)/(\cdot)$ and $\psi(0) = 1$.

Suppose $g(z_1) = g(z_2)$. Then $z_1\psi(z_1^2) = z_2\psi(z_2^2)$.

Squaring: $z_1^2\psi(z_1^2)^2 = z_2^2\psi(z_2^2)^2$, i.e., $z_1^2 \cdot f(z_1^2)/z_1^2 = z_2^2 \cdot f(z_2^2)/z_2^2$, i.e., $f(z_1^2) = f(z_2^2)$.

Since $f$ is injective: $z_1^2 = z_2^2$, so $z_1 = \pm z_2$.

Case 1: $z_1 = z_2$. Done.
Case 2: $z_1 = -z_2 \neq 0$. Then $g(z_1) = g(-z_1)$, i.e., $z_1\psi(z_1^2) = -z_1\psi(z_1^2)$ (since $(-z_1)^2 = z_1^2$). This gives $2z_1\psi(z_1^2) = 0$. Since $z_1 \neq 0$ and $\psi(z_1^2) \neq 0$ (because $\psi^2(z_1^2) = f(z_1^2)/z_1^2$ and $f(z_1^2) \neq 0$ since $f$ is injective and $f(0) = 0$ with $z_1^2 \neq 0$), we get a contradiction.

So $g$ is injective. ✓

Also, $g$ is odd: $g(-z) = -z\psi(z^2) = -g(z)$. ✓

Now let me also think about whether $g$ maps $\mathbb{D}$ to $\mathbb{C}$ with $g(0) = 0$ and $g'(0) = 1$. Yes: $g(0) = 0 \cdot \psi(0) = 0$, and $g'(z) = \psi(z^2) + z \cdot 2z\psi'(z^2)$, so $g'(0) = \psi(0) = 1$. ✓

Everything checks out. Let me now write the final solution.

---

## Model Solution

# Koebe–Bieberbach Radius Theorem: Complete Proof

## Part (a): No uniform $r$ exists without further restrictions

**Proof.** Define $f_n(z) = z/n$ for $n = 1, 2, 3, \ldots$

Each $f_n$ is holomorphic on $\mathbb{D}$ with $f_n(0) = 0$, and
$$f_n(\mathbb{D}) = \left\{\frac{z}{n} : |z| < 1\right\} = D_{1/n}(0).$$
Since $|1/n| = 1/n$, the point $1/n$ lies on the boundary of this open disk, so $1/n \notin f_n(\mathbb{D})$.

We compute $f_n'(0) = 1/n \to 0$. For any proposed $r > 0$, choose $n$ with $1/n < r$; then $1/n \in D_r(0)$ but $1/n \notin f_n(\mathbb{D})$, so no such $r$ exists. $\blacksquare$

## Part (b): No uniform $r$ exists even with $f'(0) = 1$

**Proof.** Define $f_\epsilon(z) = \epsilon(e^{z/\epsilon} - 1)$ for $\epsilon > 0$.

- $f_\epsilon(0) = \epsilon(e^0 - 1) = 0$.
- $f_\epsilon'(z) = e^{z/\epsilon}$, so $f_\epsilon'(0) = 1$.
- $f_\epsilon$ is entire, hence holomorphic on $\mathbb{D}$.

Since $e^{z/\epsilon} \neq 0$ for all $z \in \mathbb{C}$, we have $f_\epsilon(z) = \epsilon(e^{z/\epsilon} - 1) \neq -\epsilon$ for all $z$. Thus $-\epsilon \notin f_\epsilon(\mathbb{D})$.

For any $r > 0$, choose $\epsilon < r$. Then $|-\epsilon| = \epsilon < r$, so $-\epsilon \in D_r(0)$, yet $-\epsilon \notin f_\epsilon(\mathbb{D})$. No uniform $r$ exists. $\blacksquare$

## Part (c): Area theorem — $\sum_{n=1}^{\infty} n|c_n|^2 \leq 1$

**Proof.** Let $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \cdots$ be injective on $0 < |z| < 1$. For $0 < \rho < 1$, consider $h$ on the punctured disk $D_\rho(0)\setminus\{0\}$.

**Step 1 (Change of variable).** Set $w = 1/z$ and define $G(w) = h(1/w) = w + c_0 + c_1/w + c_2/w^2 + \cdots$, which is injective on $\{|w| > 1/\rho\}$. As $z \to 0$, $h(z) \to \infty$, so $h(D_\rho(0)\setminus\{0\})$ is unbounded with compact complement $K_\rho$.

**Step 2 (Area computation).** For $R > 1/\rho$, compute the signed area enclosed by the Jordan curve $\Gamma_R = G(\{|w| = R\})$ using:
$$A(R) = \frac{1}{2i}\oint_{|w|=R} \overline{G(w)}\, G'(w)\, dw.$$

Writing $G(w) = \sum_n a_n w^n$ (with $a_1 = 1$, $a_{-n} = c_n$), and using $\bar{w} = R^2/w$ on $|w|=R$, the integrand $\overline{G(w)}G'(w)$ has Laurent expansion whose $w^{-1}$ coefficient is $\sum_n n|a_n|^2 R^{2n}$. By the residue theorem:
$$A(R) = \pi\left(R^2 - \sum_{n=1}^{\infty} n|c_n|^2 R^{-2n}\right).$$

**Step 3 (Area of complement).** The enclosed area decomposes as $A(R) = \text{Area}(K_\rho) + \text{Area}(G(\{1/\rho < |w| < R\}))$. As $R \to (1/\rho)^+$, the annular contribution vanishes, giving:
$$\text{Area}(K_\rho) = \pi\left(\frac{1}{\rho^2} - \sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n}\right).$$

**Step 4 (Conclusion).** Since Area$(K_\rho) \geq 0$, we get $\sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n} \leq 1/\rho^2$ for all $\rho \in (0,1)$. Letting $\rho \to 1^-$ (by monotone convergence):
$$\boxed{\sum_{n=1}^{\infty} n|c_n|^2 \leq 1.} \qquad \blacksquare$$

## Part (d): Existence of $g$ with $g^2(z) = f(z^2)$

**Proof.** Let $f(z) = z + a_2 z^2 + \cdots$ be injective on $\mathbb{D}$ with $f(0) = 0$, $f'(0) = 1$.

**Step 1 ($f(z)/z$ never vanishes).** Since $f(z) = z(1 + a_2 z + \cdots)$, clearly $f(z)/z \neq 0$ near 0. For $z \neq 0$: if $f(z)/z = 0$ then $f(z) = 0 = f(0)$, contradicting injectivity. So $f(z)/z \neq 0$ on all of $\mathbb{D}$.

**Step 2 (Holomorphic square root).** Since $\mathbb{D}$ is simply connected and $f(z)/z$ is holomorphic and nowhere vanishing, there exists a holomorphic square root $\psi$ on $\mathbb{D}$ with $\psi^2(z) = f(z)/z$ and $\psi(0) = 1$.

**Step 3 (Definition and properties of $g$).** Define $g(z) = z\psi(z^2)$. Then:
$$g(z)^2 = z^2\psi(z^2)^2 = z^2 \cdot \frac{f(z^2)}{z^2} = f(z^2).$$
Also $g(0) = 0$ and $g'(0) = \psi(0) = 1$.

**Step 4 (Injectivity of $g$).** Suppose $g(z_1) = g(z_2)$. Squaring gives $f(z_1^2) = f(z_2^2)$, so by injectivity of $f$: $z_1^2 = z_2^2$, hence $z_1 = \pm z_2$. If $z_1 = -z_2 \neq 0$, then $g(z_1) = g(-z_1)$ gives $z_1\psi(z_1^2) = -z_1\psi(z_1^2)$ (using $g$ is odd since $g(-z) = -z\psi(z^2) = -g(z)$). This forces $2z_1\psi(z_1^2) = 0$. But $z_1 \neq 0$ and $\psi(z_1^2) \neq 0$ (since $\psi^2(z_1^2) = f(z_1^2)/z_1^2 \neq 0$ because $f(z_1^2) \neq 0$ by injectivity). Contradiction. Hence $z_1 = z_2$, and $g$ is injective. $\blacksquare$

## Part (e): $|a_2| \leq 2$ with equality characterization

**Proof.**

**Step 1 (Structure of $g$).** From part (d), $g(z) = z\psi(z^2)$ where $\psi(z) = \sqrt{f(z)/z}$. Writing $\psi(z) = 1 + \frac{a_2}{2}z + \cdots$ (from $\psi^2 = 1 + a_2 z + \cdots$), we get:
$$g(z) = z + \frac{a_2}{2}z^3 + \cdots$$
which is an odd function with $g'(0) = 1$.

**Step 2 (Apply area theorem to $1/g$).** Since $g$ is injective on $\mathbb{D}$ with $g(0) = 0$, the function $1/g$ is injective on $\mathbb{D}\setminus\{0\}$ with a simple pole at 0:
$$\frac{1}{g(z)} = \frac{1}{z} - \frac{a_2}{2}z + \cdots$$
(using $g(z) = z(1 + \frac{a_2}{2}z^2 + \cdots)$, so $1/g = z^{-1}(1 - \frac{a_2}{2}z^2 + \cdots)$).

This has the form $1/z + d_0 + d_1 z + \cdots$ with $d_1 = -a_2/2$. By part (c):
$$|d_1|^2 \leq \sum_{n=1}^{\infty} n|d_n|^2 \leq 1 \implies |d_1| \leq 1.$$

**Step 3 (Conclusion).** Since $d_1 = -a_2/2$:
$$|a_2| = 2|d_1| \leq 2.$$

**Step 4 (Equality case).** If $|a_2| = 2$, then $|d_1| = 1$ and equality holds in $\sum n|d_n|^2 \leq 1$. By the area theorem equality case (Area$(K) = 0$ forces $1/g(z) = 1/z + e^{i\theta}z$ for some $\theta$), we get:
$$g(z) = \frac{z}{1 + e^{i\theta}z^2}, \quad f(z^2) = g(z)^2 = \frac{z^2}{(1+e^{i\theta}z^2)^2}.$$
Substituting $z^2 \mapsto z$:
$$\boxed{f(z) = \frac{z}{(1 - e^{i\theta}z)^2}.} \qquad \blacksquare$$

## Part (f): $|z_1 - z_2| \leq 4$

**Proof.** Let $h(z) = 1/z + c_0 + c_1 z + \cdots$ be injective on $0 < |z| < 1$, avoiding values $z_1$ and $z_2$.

**Step 1 (Construct normalized univalent functions).** For $j = 1, 2$, define $\phi_j(z) = 1/(h(z) - z_j)$ on $\mathbb{D}\setminus\{0\}$. Since $h$ has a simple pole at 0:
$$\phi_j(z) = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots} = z - (c_0 - z_j)z^2 + \cdots$$
extends holomorphically to $\phi_j(0) = 0$ with $\phi_j'(0) = 1$.

**Step 2 (Injectivity).** Since $h$ is injective and $w \mapsto 1/(w - z_j)$ is injective on $\mathbb{C}\setminus\{z_j\}$ (Möbius transformation), $\phi_j$ is injective on $\mathbb{D}\setminus\{0\}$. Since $\phi_j(z) \neq 0 = \phi_j(0)$ for $z \neq 0$ (as $h(z) \neq \infty$ for $z \neq 0$), $\phi_j$ is injective on all of $\mathbb{D}$.

**Step 3 (Apply part (e)).** Each $\phi_j$ satisfies $\phi_j(0) = 0$, $\phi_j'(0) = 1$, and is injective. The coefficient of $z^2$ in $\phi_j$ is $\beta_j = z_j - c_0$. By part (e):
$$|z_j - c_0| = |\beta_j| \leq 2 \quad \text{for } j = 1, 2.$$

**Step 4 (Triangle inequality).**
$$\boxed{|z_1 - z_2| \leq |z_1 - c_0| + |c_0 - z_2| \leq 2 + 2 = 4.} \qquad \blacksquare$$

## Part (g): Completing the proof of the Koebe–Bieberbach theorem

**Theorem.** If $f: \mathbb{D} \to \mathbb{C}$ is injective, holomorphic, with $f(0) = 0$ and $f'(0) = 1$, then $D_{1/4}(0) \subseteq f(\mathbb{D})$.

**Proof.** Suppose for contradiction that some $w$ with $|w| < 1/4$ satisfies $w \notin f(\mathbb{D})$.

**Step 1 (Construct an admissible $h$).** Define $h(z) = 1/f(z)$ on $\mathbb{D}\setminus\{0\}$. Since $f$ has a simple zero at 0, $h$ has a simple pole at 0, so $h(z) = 1/z + d_0 + d_1 z + \cdots$. Since $f$ is injective and $f(z) \neq 0$ for $z \neq 0$ (injectivity with $f(0) = 0$), the map $w \mapsto 1/w$ preserves injectivity on $\mathbb{C}\setminus\{0\}$, so $h$ is injective on $\mathbb{D}\setminus\{0\}$.

**Step 2 (Identify omitted values).**
- $h$ avoids $0$: $h(z) = 0$ would require $f(z) = \infty$, impossible.
- $h$ avoids $1/w$: $h(z) = 1/w$ would require $f(z) = w$, contradicting our assumption.

**Step 3 (Apply part (f)).** By part (f) with $z_1 = 0$ and $z_2 = 1/w$:
$$|0 - 1/w| \leq 4 \implies \frac{1}{|w|} \leq 4 \implies |w| \geq \frac{1}{4}.$$

This contradicts $|w| < 1/4$. Therefore $D_{1/4}(0) \subseteq f(\mathbb{D})$.

**Step 4 (Sharpness).** The Koebe function $f(z) = z/(1-z)^2 = z + 2z^2 + 3z^3 + \cdots$ satisfies all hypotheses ($f(0) = 0$, $f'(0) = 1$, injective on $\mathbb{D}$) and maps $\mathbb{D}$ onto $\mathbb{C}\setminus(-\infty, -1/4]$. In particular, $-1/4 \notin f(\mathbb{D})$, showing $r = 1/4$ cannot be improved. $\blacksquare$

---

**Summary.** The Koebe–Bieberbach theorem is established: for univalent $f$ with $f(0) = 0$, $f'(0) = 1$, the image $f(\mathbb{D})$ always contains the disk of radius $1/4$, and this is optimal.

$\boxed{D_{1/4}(0) \subseteq f(\mathbb{D}), \text{ with } 1/4 \text{ best possible.}}$

---

## Reasoning Details (raw)

```json
[
  {
    "type": "reasoning.text",
    "text": "Let me work through each part (a) through (g) carefully and completely.\n\n## Part (a): No uniform $r$ exists without further restrictions.\n\nWe need to find holomorphic functions $f_n: \\mathbb{D} \\to \\mathbb{C}$ with $f_n(0) = 0$ such that $1/n \\notin f_n(\\mathbb{D})$.\n\nTake $f_n(z) = z/n$. Then:\n- $f_n(0) = 0$ \u2713\n- $f_n$ is holomorphic on $\\mathbb{D}$ \u2713\n- $f_n(\\mathbb{D}) = \\{z/n : |z| < 1\\} = D_{1/n}(0)$, the open disk of radius $1/n$ centered at 0.\n- The point $1/n$ has modulus $1/n$, so $1/n \\notin D_{1/n}(0)$ (since the disk is open).\n\nThus $1/n \\notin f_n(\\mathbb{D})$.\n\n$f_n'(0) = 1/n \\to 0$ as $n \\to \\infty$.\n\nFor any $r > 0$, choose $n$ large enough so that $1/n < r$. Then $1/n \\in D_r(0)$ but $1/n \\notin f_n(\\mathbb{D})$, so $D_r(0) \\not\\subseteq f_n(\\mathbb{D})$.\n\n## Part (b): No uniform $r$ exists even with $f'(0) = 1$.\n\nConsider $f_\\epsilon(z) = \\epsilon(e^{z/\\epsilon} - 1)$ for $\\epsilon > 0$.\n\n- $f_\\epsilon(0) = \\epsilon(e^0 - 1) = 0$ \u2713\n- $f_\\epsilon'(z) = e^{z/\\epsilon}$, so $f_\\epsilon'(0) = 1$ \u2713\n- $f_\\epsilon$ is holomorphic on $\\mathbb{D}$ (entire, in fact) \u2713\n\nNow, $e^{z/\\epsilon} \\neq 0$ for all $z \\in \\mathbb{C}$, so $f_\\epsilon(z) = \\epsilon(e^{z/\\epsilon} - 1) \\neq \\epsilon(0 - 1) = -\\epsilon$.\n\nThus $-\\epsilon \\notin f_\\epsilon(\\mathbb{D})$.\n\nFor any $r > 0$, choose $\\epsilon < r$. Then $|-\\epsilon| = \\epsilon < r$, so $-\\epsilon \\in D_r(0)$, but $-\\epsilon \\notin f_\\epsilon(\\mathbb{D})$. Hence $D_r(0) \\not\\subseteq f_\\epsilon(\\mathbb{D})$.\n\n## Part (c): Area theorem\n\nLet $h(z) = \\frac{1}{z} + c_0 + c_1 z + c_2 z^2 + \\cdots$ be analytic and injective for $0 < |z| < 1$.\n\nConsider $h$ restricted to $D_\\rho(0) \\setminus \\{0\\}$ for $0 < \\rho < 1$. The image $h(D_\\rho(0) \\setminus \\{0\\})$ is an open set (by the open mapping theorem applied to $h$ on the annulus).\n\n**Computing the area of the complement:**\n\nThe complement of $h(D_\\rho(0) \\setminus \\{0\\})$ in $\\hat{\\mathbb{C}}$ (or rather in $\\mathbb{C}$, since $h$ maps the punctured disk to an unbounded set) can be computed using the area formula.\n\nThe boundary of $h(D_\\rho(0) \\setminus \\{0\\})$ includes the image of $|z| = \\rho$. On $|z| = \\rho$, we have:\n$$h(z) = \\frac{1}{z} + c_0 + c_1 z + c_2 z^2 + \\cdots$$\n\nThe area of the complement of the image of the annulus $0 < |z| < \\rho$ under $h$ can be computed as follows. Consider the map $w = h(z)$. The area of the complement of $h(D_\\rho \\setminus \\{0\\})$ in $\\mathbb{C}$ is:\n\nUsing the formula for area via the Laurent series: if $h(z) = 1/z + \\sum_{n=0}^{\\infty} c_n z^n$, then the area of the complement of $h(D_\\rho \\setminus \\{0\\})$ is:\n\n$$\\text{Area}(\\text{complement}) = \\pi \\left(\\frac{1}{\\rho^2} - \\sum_{n=1}^{\\infty} n |c_n|^2 \\rho^{2n}\\right)$$\n\nLet me derive this more carefully. The area of the image of the annulus $\\rho_1 < |z| < \\rho_2$ under $h$ is given by:\n$$\\text{Area} = \\iint_{\\rho_1 < |z| < \\rho_2} |h'(z)|^2 \\, dx \\, dy$$\n\nBut since $h$ is injective on this annulus, this equals the area of $h(\\text{annulus})$.\n\nActually, let me use a different approach. Consider the complement of $h(D_\\rho \\setminus \\{0\\})$. Since $h$ maps the punctured disk to a domain whose complement is compact (because $h(z) \\to \\infty$ as $z \\to 0$), we can compute the area of the complement.\n\nFor $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \\cdots$, consider the inverse function. Near $\\infty$, $h^{-1}(w)$ behaves like $1/w$. The complement of $h(D_\\rho \\setminus \\{0\\})$ is a bounded set.\n\nLet me use the standard area theorem proof. Consider the function $\\phi(w) = 1/(h(1/w) - \\text{something})$... Actually, let me use the direct approach from the hint.\n\n**Direct computation of area of complement:**\n\nFor $0 < \\rho < 1$, consider the image of the circle $|z| = \\rho$ under $h$. This gives a Jordan curve $\\Gamma_\\rho$. The interior of $\\Gamma_\\rho$ (for small $\\rho$) is the complement of $h(D_\\rho \\setminus \\{0\\})$ (more precisely, the bounded component of the complement).\n\nThe area enclosed by $\\Gamma_\\rho$ can be computed using Green's theorem:\n$$\\text{Area} = \\frac{1}{2i} \\oint_{|z|=\\rho} \\overline{h(z)} h'(z) \\, dz$$\n\nWait, let me be more careful. The area of the complement of $h(D_\\rho \\setminus \\{0\\})$ is:\n\nSince $h(z) = 1/z + c_0 + c_1 z + \\cdots$, as $z \\to 0$, $h(z) \\to \\infty$. So $h(D_\\rho \\setminus \\{0\\})$ is an unbounded domain, and its complement is bounded.\n\nThe area of the complement is:\n$$A = \\pi \\cdot \\frac{1}{\\rho^2} - \\pi \\sum_{n=1}^{\\infty} n |c_n|^2 \\rho^{2n}$$\n\nWait, let me derive this properly.\n\nConsider the inverse function $g = h^{-1}$ defined on the complement of $h(D_\\rho \\setminus \\{0\\})$. Near infinity, $g(w) \\sim 1/w$.\n\nActually, let me use the standard approach. The area of the complement of $h(D_\\rho \\setminus \\{0\\})$ can be computed as follows.\n\nOn $|z| = \\rho$, parametrize $z = \\rho e^{i\\theta}$. Then $h(z) = \\frac{1}{\\rho} e^{-i\\theta} + c_0 + c_1 \\rho e^{i\\theta} + c_2 \\rho^2 e^{2i\\theta} + \\cdots$\n\nThe area enclosed by the curve $w(\\theta) = h(\\rho e^{i\\theta})$ (which bounds the complement) is:\n\n$$A = \\frac{1}{2i} \\int_0^{2\\pi} \\overline{w(\\theta)} w'(\\theta) \\, d\\theta$$\n\nwhere $w(\\theta) = h(\\rho e^{i\\theta})$ and $w'(\\theta) = i\\rho e^{i\\theta} h'(\\rho e^{i\\theta})$.\n\nSo:\n$$A = \\frac{1}{2i} \\int_0^{2\\pi} \\overline{h(\\rho e^{i\\theta})} \\cdot i\\rho e^{i\\theta} h'(\\rho e^{i\\theta}) \\, d\\theta = \\frac{\\rho}{2} \\int_0^{2\\pi} \\overline{h(\\rho e^{i\\theta})} h'(\\rho e^{i\\theta}) e^{i\\theta} \\, d\\theta$$\n\nHmm, this is getting complicated. Let me use a cleaner approach.\n\n**Cleaner approach using the area formula:**\n\nFor an injective analytic function $h(z) = 1/z + \\sum_{n=0}^{\\infty} c_n z^n$ on $|z| < \\rho$, the area of the complement of $h(D_\\rho \\setminus \\{0\\})$ is:\n\nWe use the fact that for a univalent function $g(w) = w + b_0 + b_1/w + \\cdots$ defined near infinity, the area of the complement of $g$'s image is $\\pi \\sum_{n=1}^{\\infty} n |b_n|^2$.\n\nLet $w = 1/z$, so $z = 1/w$. When $|z| < \\rho$, we have $|w| > 1/\\rho$. Define:\n$$G(w) = h(1/w) = w + c_0 + c_1/w + c_2/w^2 + \\cdots$$\n\nThis is defined for $|w| > 1/\\rho$ and is injective. $G(w) \\to \\infty$ as $w \\to \\infty$.\n\nThe image $G(\\{|w| > 1/\\rho\\})$ equals $h(D_\\rho \\setminus \\{0\\})$.\n\nThe complement of $G(\\{|w| > 1/\\rho\\})$ in $\\mathbb{C}$ is a bounded set. Let's call it $K$.\n\nNow, $G(w) = w + c_0 + c_1/w + c_2/w^2 + \\cdots$ for $|w| > 1/\\rho$.\n\nThe area of the complement of the image of $\\{|w| = R\\}$ (for $R > 1/\\rho$) under $G$ is:\n\nUsing the area theorem for functions of the form $G(w) = w + c_0 + c_1/w + c_2/w^2 + \\cdots$ on $|w| = R$:\n\nThe area enclosed by $G(|w| = R)$ (the image curve) is:\n$$\\text{Area enclosed} = \\pi R^2 - \\pi \\sum_{n=1}^{\\infty} n |c_n|^2 R^{-2n}$$\n\nWait, let me be more precise. For $G(w) = w + \\sum_{n=0}^{\\infty} c_n w^{-n}$ on $|w| = R$:\n\n$$\\frac{1}{2i} \\oint_{|w|=R} \\overline{G(w)} G'(w) \\, dw$$\n\n$G'(w) = 1 - c_1/w^2 - 2c_2/w^3 - \\cdots$\n\n$\\overline{G(w)} = \\overline{w} + \\overline{c_0} + \\overline{c_1} \\overline{w}^{-1} + \\cdots$\n\nOn $|w| = R$: $\\overline{w} = R^2/w$, so $\\overline{G(w)} = R^2/w + \\overline{c_0} + \\overline{c_1} R^2/w + \\cdots$\n\nHmm, this is getting messy. Let me use the standard result directly.\n\n**Standard Area Theorem:** For $G(w) = w + b_0 + b_1/w + b_2/w^2 + \\cdots$ univalent in $|w| > R_0$, the area of the complement of $G(\\{|w| > R_0\\})$ is:\n$$\\pi \\sum_{n=1}^{\\infty} n |b_n|^2 R_0^{-2n}$$\n\nWait no. Let me think again.\n\nActually, the standard result is: if $G(w) = w + b_0 + b_1/w + b_2/w^2 + \\cdots$ is univalent in $|w| > 1$ (say), then $\\sum_{n=1}^{\\infty} n|b_n|^2 \\leq 1$.\n\nThe proof goes: the area of the complement of $G(\\{|w| > 1\\})$ equals $\\pi(1 - \\sum_{n=1}^{\\infty} n|b_n|^2) \\geq 0$, hence $\\sum n|b_n|^2 \\leq 1$.\n\nLet me derive this. On $|w| = R$ (large), $G(w) = w + b_0 + b_1/w + \\cdots$. The area enclosed by the image curve $G(Re^{i\\theta})$, $\\theta \\in [0, 2\\pi]$, is:\n\n$$A(R) = \\frac{1}{2i} \\int_0^{2\\pi} \\overline{G(Re^{i\\theta})} G'(Re^{i\\theta}) \\cdot iRe^{i\\theta} \\, d\\theta$$\n\nWait, more carefully: if $\\gamma(t) = G(Re^{it})$ for $t \\in [0, 2\\pi]$, then the signed area enclosed is:\n$$A = \\frac{1}{2i} \\oint_\\gamma \\bar{w} \\, dw = \\frac{1}{2i} \\int_0^{2\\pi} \\overline{G(Re^{it})} G'(Re^{it}) iRe^{it} \\, dt$$\n\nLet me write $w = Re^{it}$, $dw = iRe^{it} dt$.\n\n$$A = \\frac{1}{2i} \\int_0^{2\\pi} \\overline{G(w)} G'(w) \\, dw$$\n\nwhere the integral is over $|w| = R$.\n\n$G(w) = w + b_0 + b_1/w + b_2/w^2 + \\cdots$\n$G'(w) = 1 - b_1/w^2 - 2b_2/w^3 - \\cdots$\n\nOn $|w| = R$: $\\bar{w} = R^2/w$.\n\n$\\overline{G(w)} = \\bar{w} + \\bar{b_0} + \\bar{b_1}/\\bar{w} + \\bar{b_2}/\\bar{w}^2 + \\cdots = R^2/w + \\bar{b_0} + \\bar{b_1}R^2/w + \\bar{b_2}R^4/w^2 + \\cdots$\n\nWait, $\\bar{w} = R^2/w$ on $|w| = R$. And $\\bar{b_n}/\\bar{w}^n = \\bar{b_n} \\cdot w^n / R^{2n}$.\n\nSo $\\overline{G(w)} = R^2/w + \\bar{b_0} + \\bar{b_1}w/R^2 + \\bar{b_2}w^2/R^4 + \\cdots$\n\nNow:\n$$\\overline{G(w)} G'(w) = \\left(\\frac{R^2}{w} + \\bar{b_0} + \\frac{\\bar{b_1}w}{R^2} + \\frac{\\bar{b_2}w^2}{R^4} + \\cdots\\right)\\left(1 - \\frac{b_1}{w^2} - \\frac{2b_2}{w^3} - \\cdots\\right)$$\n\nWe need $\\frac{1}{2i}\\oint_{|w|=R} \\overline{G(w)} G'(w) dw$. Only the residue (coefficient of $1/w$) in the Laurent expansion of $\\overline{G(w)} G'(w)$ contributes.\n\nThe coefficient of $1/w$ in $\\overline{G(w)} G'(w)$:\n\nFrom $R^2/w \\cdot 1$: gives $R^2/w$. Coefficient of $1/w$: $R^2$.\n\nFrom $\\bar{b_0} \\cdot (-b_1/w^2)$: gives $-\\bar{b_0}b_1/w^2$. Not $1/w$.\n\nFrom $\\bar{b_1}w/R^2 \\cdot (-b_1/w^2) = -\\bar{b_1}b_1/(R^2 w)$: Coefficient of $1/w$: $-|b_1|^2/R^2$.\n\nFrom $\\bar{b_2}w^2/R^4 \\cdot (-2b_2/w^3) = -2\\bar{b_2}b_2/(R^4 w) = -2|b_2|^2/R^4$: Coefficient of $1/w$: $-2|b_2|^2/R^4$.\n\nIn general, from $\\bar{b_n}w^n/R^{2n} \\cdot (-nb_n/w^{n+1}) = -n|b_n|^2/(R^{2n}w)$: Coefficient of $1/w$: $-n|b_n|^2/R^{2n}$.\n\nSo the residue at $\\infty$ (or rather, the coefficient of $1/w$) is:\n$$R^2 - \\sum_{n=1}^{\\infty} \\frac{n|b_n|^2}{R^{2n}}$$\n\nTherefore:\n$$A(R) = \\frac{1}{2i} \\cdot 2\\pi i \\left(R^2 - \\sum_{n=1}^{\\infty} \\frac{n|b_n|^2}{R^{2n}}\\right) = \\pi\\left(R^2 - \\sum_{n=1}^{\\infty} \\frac{n|b_n|^2}{R^{2n}}\\right)$$\n\nThis is the signed area enclosed by the image curve $G(|w| = R)$. Since $G$ is injective, this equals the area of the region enclosed.\n\nNow, for our situation: $G(w) = h(1/w) = w + c_0 + c_1/w + c_2/w^2 + \\cdots$ defined for $|w| > 1/\\rho$.\n\nThe image $G(\\{|w| > 1/\\rho\\}) = h(D_\\rho \\setminus \\{0\\})$.\n\nThe complement of this image is a bounded set. As $R \\to 1/\\rho$ from above, the image curve $G(|w| = R)$ approaches the boundary of the image of $|z| = \\rho$ under $h$.\n\nActually, let me reconsider. The area of the complement of $h(D_\\rho \\setminus \\{0\\})$ is what we want.\n\n$G$ maps $\\{|w| > 1/\\rho\\}$ to some domain. The complement of this domain is bounded. The area of the complement is:\n\nAs $R \\to \\infty$, $A(R) \\to \\infty$ (it's approximately $\\pi R^2$). The area enclosed by $G(|w| = R)$ is the area of the image of $\\{|w| < R\\}$ under $G$... no wait, it's the area enclosed by the curve $G(|w| = R)$.\n\nHmm, let me think about this differently. $G$ maps $\\{|w| > 1/\\rho\\}$ conformally onto some domain $\\Omega$. The complement $\\mathbb{C} \\setminus \\Omega$ is compact. The area of $\\mathbb{C} \\setminus \\Omega$ is what we want.\n\nThe curve $G(|w| = R)$ for $R > 1/\\rho$ lies in $\\Omega$ and encloses a region that contains $\\mathbb{C} \\setminus \\Omega$ in its interior (for large enough $R$... actually for any $R > 1/\\rho$ since $G$ is injective).\n\nWait, actually: $G(|w| = R)$ for $R > 1/\\rho$ is a Jordan curve. The interior of this curve contains $\\mathbb{C} \\setminus G(\\{|w| > R\\})$... hmm no.\n\nLet me think again. $G$ maps $\\{|w| > 1/\\rho\\}$ injectively to $\\Omega$. As $|w| \\to \\infty$, $G(w) \\to \\infty$. So $\\Omega$ is an unbounded domain. Its complement $K = \\mathbb{C} \\setminus \\Omega$ is compact.\n\nFor $R > 1/\\rho$, the curve $\\Gamma_R = G(|w| = R)$ lies in $\\Omega$. The interior of $\\Gamma_R$ contains $K$ (since $K$ is bounded and lies in the complement of $G(\\{|w| > R\\})$, and by continuity/jordan curve theorem).\n\nThe area enclosed by $\\Gamma_R$ equals:\n- Area of $K$ + Area of $G(\\{1/\\rho < |w| < R\\})$\n\nSo: $A(R) = \\text{Area}(K) + \\text{Area}(G(\\{1/\\rho < |w| < R\\}))$\n\nAnd $\\text{Area}(G(\\{1/\\rho < |w| < R\\})) = \\int_{1/\\rho}^{R} \\int_0^{2\\pi} |G'(Re^{i\\theta})|^2 R \\, dR \\, d\\theta$... no, that's not right either.\n\nActually: $\\text{Area}(G(\\{1/\\rho < |w| < R\\})) = \\int_{1/\\rho < |w| < R} |G'(w)|^2 \\, dx \\, dy$\n\nwhere $w = x + iy$. In polar coordinates:\n$$= \\int_{1/\\rho}^{R} \\int_0^{2\\pi} |G'(re^{i\\theta})|^2 r \\, d\\theta \\, dr$$\n\nBut also, the signed area formula gives:\n$$A(R) = \\pi\\left(R^2 - \\sum_{n=1}^{\\infty} \\frac{n|b_n|^2}{R^{2n}}\\right)$$\n\nwhere $b_n = c_n$ in our case.\n\nAnd $A(R) = \\text{Area}(K) + \\text{Area}(G(\\{1/\\rho < |w| < R\\}))$.\n\nAs $R \\to 1/\\rho^+$, $A(R) \\to \\text{Area}(K)$ (since the annular area goes to 0).\n\nSo: $\\text{Area}(K) = \\lim_{R \\to (1/\\rho)^+} \\pi\\left(R^2 - \\sum_{n=1}^{\\infty} \\frac{n|c_n|^2}{R^{2n}}\\right) = \\pi\\left(\\frac{1}{\\rho^2} - \\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n}\\right)$\n\nSince Area$(K) \\geq 0$:\n$$\\frac{1}{\\rho^2} - \\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n} \\geq 0$$\n$$\\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n} \\leq \\frac{1}{\\rho^2}$$\n\nLetting $\\rho \\to 1^-$:\n$$\\sum_{n=1}^{\\infty} n|c_n|^2 \\leq 1$$\n\nThis proves part (c).\n\n## Part (d): Existence of $g$ with $g^2(z) = f(z^2)$\n\nGiven $f(z) = z + a_2 z^2 + a_3 z^3 + \\cdots$ is injective on $\\mathbb{D}$, $f(0) = 0$, $f'(0) = 1$.\n\n**Step 1:** $f(z)/z = 1 + a_2 z + a_3 z^2 + \\cdots$ is holomorphic on $\\mathbb{D}$.\n\nWe need to show $f(z)/z \\neq 0$ on $\\mathbb{D}$. Since $f(0) = 0$ and $f'(0) = 1 \\neq 0$, by continuity $f(z)/z \\neq 0$ near 0. For $z \\neq 0$, if $f(z)/z = 0$ then $f(z) = 0 = f(0)$, contradicting injectivity. So $f(z)/z \\neq 0$ on all of $\\mathbb{D}$.\n\n**Step 2:** Since $\\mathbb{D}$ is simply connected and $f(z)/z$ is holomorphic and nowhere vanishing, there exists a holomorphic square root $\\psi(z)$ with $\\psi(z)^2 = f(z)/z$ and $\\psi(0) = 1$ (choosing the branch with $\\psi(0) = 1$ since $f(0)/0 = 1$ in the limit).\n\n**Step 3:** Define $g(z) = z\\psi(z^2)$. Then:\n$$g(z)^2 = z^2 \\psi(z^2)^2 = z^2 \\cdot \\frac{f(z^2)}{z^2} = f(z^2)$$\n\n**Step 4:** $g(0) = 0$ and $g'(0) = \\psi(0) = 1$.\n\n**Step 5:** $g$ is injective. Suppose $g(z_1) = g(z_2)$. Then $g(z_1)^2 = g(z_2)^2$, so $f(z_1^2) = f(z_2^2)$. Since $f$ is injective, $z_1^2 = z_2^2$, so $z_1 = \\pm z_2$.\n\nIf $z_1 = -z_2 \\neq 0$, then $g(z_1) = g(-z_1)$, so $z_1 \\psi(z_1^2) = -z_1 \\psi(z_1^2)$, which gives $2z_1\\psi(z_1^2) = 0$. Since $z_1 \\neq 0$ and $\\psi(z_1^2) \\neq 0$ (because $\\psi^2(z_1^2) = f(z_1^2)/z_1^2 \\neq 0$ as $f(z_1^2) \\neq 0$ for $z_1^2 \\neq 0$), this is a contradiction. So $z_1 = z_2$.\n\nWait, I need to be more careful. $\\psi(z_1^2) \\neq 0$ because $\\psi^2(z_1^2) = f(z_1^2)/z_1^2$ and $f(z_1^2) \\neq 0$ (since $f$ is injective and $f(0) = 0$, and $z_1^2 \\neq 0$). So indeed $\\psi(z_1^2) \\neq 0$, contradiction.\n\nAlso, $g$ is odd: $g(-z) = -z\\psi((-z)^2) = -z\\psi(z^2) = -g(z)$.\n\n## Part (e): $|a_2| \\leq 2$ with equality characterization\n\n**Step 1:** Since $g$ is injective with $g(0) = 0$, $g'(0) = 1$, and $g$ is odd (as shown above), $g(z) = z + b_3 z^3 + b_5 z^5 + \\cdots$ (only odd powers).\n\nFrom $g(z) = z\\psi(z^2)$ and $\\psi(z) = 1 + \\frac{a_2}{2}z + \\frac{a_3}{2}z^2 + \\cdots$ (since $\\psi^2(z) = f(z)/z = 1 + a_2 z + a_3 z^2 + \\cdots$, and $\\psi(z) = 1 + \\frac{a_2}{2}z + \\cdots$ by expanding the square root):\n\nActually, let me compute $\\psi$ more carefully. $\\psi(z)^2 = 1 + a_2 z + a_3 z^2 + \\cdots$. Writing $\\psi(z) = 1 + \\alpha_1 z + \\alpha_2 z^2 + \\cdots$:\n$(1 + \\alpha_1 z + \\alpha_2 z^2 + \\cdots)^2 = 1 + 2\\alpha_1 z + (\\alpha_1^2 + 2\\alpha_2)z^2 + \\cdots$\n\nSo $2\\alpha_1 = a_2$, giving $\\alpha_1 = a_2/2$.\n\nThen $g(z) = z\\psi(z^2) = z(1 + \\frac{a_2}{2}z^2 + \\cdots) = z + \\frac{a_2}{2}z^3 + \\cdots$\n\nSo $g(z) = z + b_3 z^3 + \\cdots$ where $b_3 = a_2/2$.\n\n**Step 2:** Consider $1/g(z)$. Since $g$ has a simple zero at 0, $1/g$ has a simple pole at 0:\n$$1/g(z) = \\frac{1}{z} + d_0 + d_1 z + d_2 z^2 + \\cdots$$\n\nSince $g(z) = z + b_3 z^3 + \\cdots$:\n$$\\frac{1}{g(z)} = \\frac{1}{z(1 + b_3 z^2 + \\cdots)} = \\frac{1}{z}(1 - b_3 z^2 + \\cdots) = \\frac{1}{z} - b_3 z + \\cdots$$\n\nSo $d_1 = -b_3 = -a_2/2$.\n\n**Step 3:** $1/g(z)$ is injective on $\\mathbb{D}$ (since $g$ is injective and $1/w$ is injective on $\\mathbb{C} \\setminus \\{0\\}$, and $g$ maps $\\mathbb{D}$ to a set not containing 0... wait, $g(0) = 0$. Let me reconsider.\n\nActually, $1/g(z)$ is defined on $\\mathbb{D} \\setminus \\{0\\}$ and is injective there. It has a simple pole at 0. So it's injective and meromorphic on $\\mathbb{D}$ with a pole at 0.\n\nTo apply part (c), we need $h$ to be injective on $0 < |z| < 1$. Indeed, $1/g(z)$ is injective on $\\mathbb{D} \\setminus \\{0\\}$ (since $g$ is injective and nonzero on $\\mathbb{D} \\setminus \\{0\\}$, and $w \\mapsto 1/w$ is injective on $\\mathbb{C} \\setminus \\{0\\}$).\n\nSo by part (c) applied to $h(z) = 1/g(z) = 1/z + d_0 + d_1 z + \\cdots$:\n$$\\sum_{n=1}^{\\infty} n|d_n|^2 \\leq 1$$\n\nIn particular, $|d_1|^2 \\leq 1$, so $|d_1| \\leq 1$.\n\nSince $d_1 = -a_2/2$, we get $|a_2/2| \\leq 1$, i.e., $|a_2| \\leq 2$.\n\n**Step 4: Equality case.** $|a_2| = 2$ iff $|d_1| = 1$ iff equality holds in $\\sum n|d_n|^2 \\leq 1$, which means $d_n = 0$ for all $n \\geq 2$ (and $|d_1| = 1$).\n\nSo $1/g(z) = 1/z + d_1 z$ with $|d_1| = 1$. Write $d_1 = e^{i\\theta}$.\n\nThen $1/g(z) = 1/z + e^{i\\theta}z$, so:\n$$g(z) = \\frac{1}{1/z + e^{i\\theta}z} = \\frac{z}{1 + e^{i\\theta}z^2}$$\n\nThen $f(z^2) = g(z)^2 = \\frac{z^2}{(1 + e^{i\\theta}z^2)^2}$.\n\nSubstituting $w = z^2$: $f(w) = \\frac{w}{(1 + e^{i\\theta}w)^2}$.\n\nSo $f(z) = \\frac{z}{(1 + e^{i\\theta}z)^2}$.\n\nWriting $e^{i\\theta} = -e^{i\\alpha}$ (i.e., replacing $\\theta$ by $\\alpha + \\pi$): $f(z) = \\frac{z}{(1 - e^{i\\alpha}z)^2}$.\n\nThis is the Koebe function (up to rotation). So equality holds iff $f(z) = \\frac{z}{(1 - e^{i\\theta}z)^2}$ for some $\\theta$.\n\n## Part (f): $|z_1 - z_2| \\leq 4$\n\nLet $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \\cdots$ be injective on $\\mathbb{D}$ and avoid values $z_1$ and $z_2$.\n\nConsider $\\phi_j(z) = 1/(h(z) - z_j)$ for $j = 1, 2$.\n\nSince $h$ avoids $z_j$, $h(z) - z_j \\neq 0$ for all $z \\in \\mathbb{D}$. Also, $h(z) - z_j$ has a simple pole at $z = 0$ (since $h$ has a simple pole at 0). So $\\phi_j(z) = 1/(h(z) - z_j)$ is holomorphic on $\\mathbb{D}$ (the pole of $h$ at 0 becomes a zero of $h(z) - z_j$ at 0, and taking the reciprocal makes it a... wait.\n\nLet me reconsider. $h(z) = 1/z + c_0 + c_1 z + \\cdots$ on $0 < |z| < 1$. Then $h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + \\cdots$, which has a simple pole at $z = 0$.\n\nSo $1/(h(z) - z_j) = \\frac{1}{1/z + (c_0 - z_j) + c_1 z + \\cdots} = \\frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \\cdots}$\n\nThis is holomorphic near 0 (the singularity at 0 is removable, and the function vanishes at 0).\n\n$\\phi_j(z) = \\frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \\cdots} = z - (c_0 - z_j)z^2 + \\cdots$\n\nSo $\\phi_j(0) = 0$ and $\\phi_j'(0) = 1$.\n\nNow, is $\\phi_j$ injective? Since $h$ is injective and $w \\mapsto 1/(w - z_j)$ is injective on $\\mathbb{C} \\setminus \\{z_j\\}$ (and $h$ avoids $z_j$), the composition $\\phi_j = 1/(h - z_j)$ is injective on $\\mathbb{D} \\setminus \\{0\\}$. And $\\phi_j$ extends holomorphically to 0 with $\\phi_j(0) = 0$.\n\nActually, we need to check that $\\phi_j$ is injective on all of $\\mathbb{D}$. Since $h$ is injective on $0 < |z| < 1$ and $\\phi_j$ is the composition of $h$ with the injective map $w \\mapsto 1/(w - z_j)$ (on the range of $h$, which avoids $z_j$), $\\phi_j$ is injective on $\\mathbb{D} \\setminus \\{0\\}$. At $z = 0$: $\\phi_j(0) = 0$, and for $z \\neq 0$, $\\phi_j(z) = 1/(h(z) - z_j) \\neq 0$ (since $h(z) - z_j \\neq \\infty$ for $z \\neq 0$... well, $h(z)$ is finite for $z \\neq 0$, so $\\phi_j(z)$ is finite and nonzero iff $h(z) \\neq \\infty$, which is true for $z \\neq 0$). Wait, $\\phi_j(z) = 0$ iff $h(z) = \\infty$, which only happens at $z = 0$. So $\\phi_j(z) \\neq 0 = \\phi_j(0)$ for $z \\neq 0$. Thus $\\phi_j$ is injective on $\\mathbb{D}$.\n\nSo $\\phi_j: \\mathbb{D} \\to \\mathbb{C}$ is holomorphic, injective, $\\phi_j(0) = 0$, $\\phi_j'(0) = 1$.\n\nWrite $\\phi_j(z) = z + \\beta_{j,2} z^2 + \\cdots$. From the expansion above: $\\beta_{j,2} = -(c_0 - z_j) = z_j - c_0$.\n\nBy part (e), $|\\beta_{j,2}| \\leq 2$, so $|z_j - c_0| \\leq 2$ for $j = 1, 2$.\n\nTherefore: $|z_1 - z_2| = |(z_1 - c_0) - (z_2 - c_0)| \\leq |z_1 - c_0| + |z_2 - c_0| \\leq 2 + 2 = 4$.\n\n## Part (g): Completing the proof\n\n**Theorem:** If $f: \\mathbb{D} \\to \\mathbb{C}$ is injective, holomorphic, with $f(0) = 0$ and $f'(0) = 1$, then $D_{1/4}(0) \\subseteq f(\\mathbb{D})$.\n\n**Proof:** Suppose for contradiction that there exists $w \\in \\mathbb{C}$ with $|w| < 1/4$ such that $w \\notin f(\\mathbb{D})$.\n\nSince $f$ is injective and $f(0) = 0$, we have $f(z) \\neq 0$ for all $z \\neq 0$ in $\\mathbb{D}$. So $0 \\notin f(\\mathbb{D} \\setminus \\{0\\})$.\n\nConsider $h(z) = 1/f(z)$, defined on $\\mathbb{D} \\setminus \\{0\\}$. Then:\n- $h$ has a simple pole at $z = 0$ (since $f$ has a simple zero at 0).\n- $h$ is injective on $\\mathbb{D} \\setminus \\{0\\}$ (since $f$ is injective and $w \\mapsto 1/w$ is injective on $\\mathbb{C} \\setminus \\{0\\}$).\n- $h$ avoids the value $0$ (since $f$ is finite, $1/f$ is never $\\infty$... wait, $h(z) = 0$ would mean $f(z) = \\infty$, which doesn't happen). Actually $h$ avoids $0$ because $f(z)$ is always finite.\n- $h$ avoids $1/w$ because $f$ avoids $w$.\n\nSo $h(z) = 1/f(z)$ is injective on $0 < |z| < 1$ and avoids the values $0$ and $1/w$.\n\nBy part (f): $|0 - 1/w| \\leq 4$, i.e., $1/|w| \\leq 4$, i.e., $|w| \\geq 1/4$.\n\nThis contradicts $|w| < 1/4$. Therefore $D_{1/4}(0) \\subseteq f(\\mathbb{D})$.\n\n**Sharpness:** The Koebe function $f(z) = z/(1-z)^2 = z + 2z^2 + 3z^3 + \\cdots$ satisfies $f(0) = 0$, $f'(0) = 1$, is injective on $\\mathbb{D}$, and its image is $\\mathbb{C} \\setminus (-\\infty, -1/4]$. So $-1/4 \\notin f(\\mathbb{D})$, showing that $r = 1/4$ is optimal.\n\nWait, let me double-check part (f) more carefully. The hint says \"Look at the second coefficient in the power series expansion of $1/(h(z) - z_j)$.\"\n\nSo in part (f), $h(z) = 1/z + c_0 + c_1 z + \\cdots$ is injective on $\\mathbb{D}$ (the problem says \"injective on $\\mathbb{D}$\" but I think it means on $0 < |z| < 1$ since $h$ has a pole at 0).\n\nActually, re-reading part (f): \"If $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \\cdots$ is injective on $\\mathbb{D}$ and avoids the values $z_1$ and $z_2$...\"\n\nI think this means $h$ is defined and injective on $\\mathbb{D} \\setminus \\{0\\}$ (or perhaps on the punctured disk $0 < |z| < 1$).\n\nThe function $\\phi_j(z) = 1/(h(z) - z_j)$:\n- At $z = 0$: $h(z) - z_j = 1/z + (c_0 - z_j) + \\cdots$, so $\\phi_j(z) = z/(1 + (c_0 - z_j)z + \\cdots) = z - (c_0 - z_j)z^2 + \\cdots$\n- $\\phi_j(0) = 0$, $\\phi_j'(0) = 1$.\n\nBy part (e), the second coefficient of $\\phi_j$ satisfies $|\\beta_{j,2}| \\leq 2$.\n\n$\\beta_{j,2} = -(c_0 - z_j) = z_j - c_0$.\n\nSo $|z_1 - c_0| \\leq 2$ and $|z_2 - c_0| \\leq 2$.\n\nBy triangle inequality: $|z_1 - z_2| \\leq |z_1 - c_0| + |c_0 - z_2| \\leq 4$. \u2713\n\nNow let me also verify the injectivity argument for $\\phi_j$ more carefully.\n\n$h: \\mathbb{D} \\setminus \\{0\\} \\to \\mathbb{C}$ is injective and avoids $z_j$. The map $w \\mapsto 1/(w - z_j)$ is injective on $\\mathbb{C} \\setminus \\{z_j\\}$ (it's a M\u00f6bius transformation). Since $h(\\mathbb{D} \\setminus \\{0\\}) \\subset \\mathbb{C} \\setminus \\{z_j\\}$, the composition $\\phi_j = 1/(h - z_j)$ is injective on $\\mathbb{D} \\setminus \\{0\\}$.\n\nNow, $\\phi_j$ extends to $z = 0$ with $\\phi_j(0) = 0$. For $z \\neq 0$, $\\phi_j(z) = 1/(h(z) - z_j)$ is finite (since $h(z)$ is finite for $z \\neq 0$) and nonzero (since $h(z) \\neq \\infty$ for $z \\neq 0$, and $h(z) - z_j \\neq 0$ since $h$ avoids $z_j$). So $\\phi_j(z) \\neq 0 = \\phi_j(0)$ for $z \\neq 0$. Thus $\\phi_j$ is injective on all of $\\mathbb{D}$. \u2713\n\nAnd $\\phi_j$ satisfies $\\phi_j(0) = 0$, $\\phi_j'(0) = 1$, and is injective. So part (e) applies. \u2713\n\nLet me now write up the complete solution more carefully.\n\nActually, let me reconsider part (c) more carefully. The hint says \"Calculate the area of the complement of $h(D_\\rho(0) - \\{0\\})$ where $0 < \\rho < 1$, and let $\\rho \\to 1$.\"\n\nSo we need to compute the area of the complement of $h(\\{0 < |z| < \\rho\\})$ for $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \\cdots$ injective on $0 < |z| < 1$.\n\n$h$ maps the punctured disk $D_\\rho(0) \\setminus \\{0\\}$ to some domain. Since $h(z) \\to \\infty$ as $z \\to 0$, the image is unbounded, and its complement in $\\mathbb{C}$ is a compact set (let's call it $K_\\rho$).\n\nTo compute the area of $K_\\rho$, we use the substitution $w = 1/z$. Let $G(w) = h(1/w) = w + c_0 + c_1/w + c_2/w^2 + \\cdots$. This is defined for $|w| > 1/\\rho$.\n\n$G$ maps $\\{|w| > 1/\\rho\\}$ to the same image as $h$ maps $\\{0 < |z| < \\rho\\}$, i.e., $G(\\{|w| > 1/\\rho\\}) = h(D_\\rho(0) \\setminus \\{0\\})$.\n\nThe complement of this image is $K_\\rho$.\n\nNow, for $R > 1/\\rho$, the image of the circle $|w| = R$ under $G$ is a Jordan curve $\\Gamma_R$. The area enclosed by $\\Gamma_R$ equals:\n\n$$\\text{Area enclosed by } \\Gamma_R = \\pi\\left(R^2 - \\sum_{n=1}^{\\infty} n|c_n|^2 R^{-2n}\\right)$$\n\n(This is the standard formula derived above.)\n\nThis enclosed area = Area$(K_\\rho)$ + Area$(G(\\{1/\\rho < |w| < R\\}))$.\n\nAs $R \\to (1/\\rho)^+$:\n- Area enclosed by $\\Gamma_R \\to$ Area$(K_\\rho)$ (since the annular region shrinks to zero)\n- $\\pi\\left(R^2 - \\sum_{n=1}^{\\infty} n|c_n|^2 R^{-2n}\\right) \\to \\pi\\left(1/\\rho^2 - \\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n}\\right)$\n\nSo Area$(K_\\rho) = \\pi\\left(1/\\rho^2 - \\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n}\\right) \\geq 0$.\n\nThis gives $\\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n} \\leq 1/\\rho^2$.\n\nAs $\\rho \\to 1^-$: $\\sum_{n=1}^{\\infty} n|c_n|^2 \\leq 1$. \u2713\n\nNow let me also think about whether the formula for the area enclosed by $\\Gamma_R$ needs more justification.\n\nThe signed area enclosed by a Jordan curve $\\gamma(t) = G(Re^{it})$, $t \\in [0, 2\\pi]$, is:\n$$A = \\frac{1}{2i} \\oint_{\\Gamma_R} \\bar{w} \\, dw = \\frac{1}{2i} \\int_0^{2\\pi} \\overline{G(Re^{it})} G'(Re^{it}) iRe^{it} \\, dt$$\n\n$= \\frac{1}{2} \\int_0^{2\\pi} \\overline{G(Re^{it})} G'(Re^{it}) Re^{it} \\, dt$\n\nHmm, let me use the complex integral form. For a curve $\\gamma(t) = x(t) + iy(t)$:\n$$\\text{Area} = \\frac{1}{2} \\int_0^{2\\pi} (x\\dot{y} - y\\dot{x}) \\, dt = \\frac{1}{2i} \\int_0^{2\\pi} \\bar{\\gamma} \\dot{\\gamma} \\, dt$$\n\nWith $\\gamma(t) = G(Re^{it})$, $\\dot{\\gamma}(t) = G'(Re^{it}) \\cdot iRe^{it}$.\n\n$$\\text{Area} = \\frac{1}{2i} \\int_0^{2\\pi} \\overline{G(Re^{it})} G'(Re^{it}) iRe^{it} \\, dt = \\frac{R}{2} \\int_0^{2\\pi} \\overline{G(Re^{it})} G'(Re^{it}) e^{it} \\, dt$$\n\nAlternatively, using complex variable notation with $w = Re^{it}$:\n$$\\text{Area} = \\frac{1}{2i} \\oint_{|w|=R} \\overline{G(w)} G'(w) \\, dw$$\n\nWait, $dw = iRe^{it} dt$, so $dt = dw/(iRe^{it}) = dw/(iw)$. And:\n$$\\text{Area} = \\frac{1}{2i} \\int \\overline{G(w)} G'(w) \\cdot \\frac{dw}{iw} \\cdot iw$$\n\nHmm, let me just do it directly.\n\n$$\\text{Area} = \\frac{1}{2i} \\oint_{|w|=R} \\overline{G(w)} G'(w) \\, dw$$\n\nWait no. Let me redo this. The area formula for a parametrized curve $\\gamma(t) = G(R e^{it})$, $t \\in [0, 2\\pi]$:\n\n$$A = \\frac{1}{2i} \\int_0^{2\\pi} \\overline{\\gamma(t)} \\gamma'(t) \\, dt$$\n\n$\\gamma'(t) = G'(Re^{it}) \\cdot iRe^{it}$\n\n$A = \\frac{1}{2i} \\int_0^{2\\pi} \\overline{G(Re^{it})} G'(Re^{it}) iRe^{it} \\, dt$\n\nNow substitute $w = Re^{it}$, $dw = iRe^{it} dt$, so $dt = dw/(iRe^{it}) = dw/(iw)$:\n\n$A = \\frac{1}{2i} \\oint_{|w|=R} \\overline{G(w)} G'(w) \\frac{dw}{iw} \\cdot iw$\n\nHmm, this isn't simplifying nicely. Let me just compute directly.\n\n$A = \\frac{1}{2i} \\int_0^{2\\pi} \\overline{G(Re^{it})} G'(Re^{it}) iRe^{it} \\, dt$\n\n$= \\frac{R}{2} \\int_0^{2\\pi} \\overline{G(Re^{it})} G'(Re^{it}) e^{it} \\, dt$\n\nLet me write $G(w) = \\sum_{n=-\\infty}^{\\infty} a_n w^n$ where $a_1 = 1$, $a_0 = c_0$, $a_{-n} = c_n$ for $n \\geq 1$.\n\nOn $|w| = R$: $\\bar{w} = R^2/w$, so $\\bar{w}^n = R^{2n}/w^n$.\n\n$\\overline{G(w)} = \\sum_n \\bar{a}_n \\bar{w}^n = \\sum_n \\bar{a}_n R^{2n}/w^n$\n\n$G'(w) = \\sum_n n a_n w^{n-1}$\n\n$\\overline{G(w)} G'(w) = \\left(\\sum_n \\bar{a}_n R^{2n} w^{-n}\\right) \\left(\\sum_m m a_m w^{m-1}\\right)$\n\nThe integral $\\frac{R}{2} \\int_0^{2\\pi} \\overline{G(Re^{it})} G'(Re^{it}) e^{it} \\, dt$ with $w = Re^{it}$, $e^{it} = w/R$:\n\n$= \\frac{R}{2} \\int_0^{2\\pi} \\overline{G(w)} G'(w) \\frac{w}{R} \\, dt = \\frac{1}{2} \\int_0^{2\\pi} \\overline{G(w)} G'(w) w \\, dt$\n\n$= \\frac{1}{2} \\oint_{|w|=R} \\overline{G(w)} G'(w) w \\frac{dw}{iw}$\n\n$= \\frac{1}{2i} \\oint_{|w|=R} \\overline{G(w)} G'(w) \\, dw$\n\nOK so the area is:\n$$A = \\frac{1}{2i} \\oint_{|w|=R} \\overline{G(w)} G'(w) \\, dw$$\n\nNow, $\\overline{G(w)} G'(w) = \\left(\\sum_n \\bar{a}_n R^{2n} w^{-n}\\right)\\left(\\sum_m m a_m w^{m-1}\\right)$\n\nThe integral picks out the coefficient of $w^{-1}$ (residue theorem: $\\oint w^k dw = 2\\pi i$ if $k = -1$, else 0).\n\nWe need $-n + m - 1 = -1$, i.e., $m = n$.\n\nCoefficient of $w^{-1}$: $\\sum_n \\bar{a}_n R^{2n} \\cdot n a_n = \\sum_n n |a_n|^2 R^{2n}$\n\nSo: $A = \\frac{1}{2i} \\cdot 2\\pi i \\sum_n n|a_n|^2 R^{2n} = \\pi \\sum_n n|a_n|^2 R^{2n}$\n\nBut wait, we need to be careful about which $n$ contribute. $a_n$ for our function $G$:\n- $a_1 = 1$ (coefficient of $w$)\n- $a_0 = c_0$ (constant term)\n- $a_{-n} = c_n$ for $n \\geq 1$ (coefficient of $w^{-n}$)\n\nSo $\\sum_n n|a_n|^2 R^{2n} = 1 \\cdot |a_1|^2 R^2 + 0 \\cdot |a_0|^2 + \\sum_{n \\geq 1} (-n)|a_{-n}|^2 R^{-2n}$\n\nWait, $n$ ranges over all integers. For $n \\geq 2$: $|a_n|^2 R^{2n}$ with $a_n$ being the coefficient of $w^n$ (which is 0 for $n \\geq 2$ in our case). For $n = 1$: $|a_1|^2 R^2 = R^2$. For $n = 0$: contributes 0. For $n \\leq -1$: $n|a_n|^2 R^{2n}$ with $a_n = c_{-n}$ for $n = -1, -2, \\ldots$\n\nSo $\\sum_{n=-\\infty}^{\\infty} n|a_n|^2 R^{2n} = R^2 + \\sum_{n=1}^{\\infty} (-n)|c_n|^2 R^{-2n} = R^2 - \\sum_{n=1}^{\\infty} n|c_n|^2 R^{-2n}$\n\nTherefore: $A(R) = \\pi(R^2 - \\sum_{n=1}^{\\infty} n|c_n|^2 R^{-2n})$\n\nThis is the area enclosed by $\\Gamma_R = G(|w| = R)$.\n\nNow, as I argued before, this equals Area$(K_\\rho)$ + Area$(G(\\{1/\\rho < |w| < R\\}))$.\n\nAs $R \\to (1/\\rho)^+$: $A(R) \\to \\pi(1/\\rho^2 - \\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n})$.\n\nAnd Area$(G(\\{1/\\rho < |w| < R\\})) \\to 0$.\n\nSo Area$(K_\\rho) = \\pi(1/\\rho^2 - \\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n}) \\geq 0$.\n\nHence $\\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n} \\leq 1/\\rho^2$.\n\nAs $\\rho \\to 1^-$: $\\sum_{n=1}^{\\infty} n|c_n|^2 \\leq 1$. \u2713\n\nGreat, this confirms part (c).\n\nNow let me also verify part (f) more carefully.\n\nIn part (f), we have $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \\cdots$ injective on $0 < |z| < 1$, avoiding values $z_1, z_2$.\n\nFor $j = 1, 2$, define $\\phi_j(z) = 1/(h(z) - z_j)$ for $z \\in \\mathbb{D} \\setminus \\{0\\}$.\n\n$h(z) - z_j = 1/z + (c_0 - z_j) + c_1 z + \\cdots$\n\n$\\phi_j(z) = \\frac{1}{1/z + (c_0 - z_j) + c_1 z + \\cdots} = \\frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \\cdots}$\n\nSo $\\phi_j$ extends to $z = 0$ with $\\phi_j(0) = 0$.\n\n$\\phi_j(z) = z \\cdot \\frac{1}{1 + (c_0 - z_j)z + \\cdots} = z(1 - (c_0 - z_j)z + \\cdots) = z - (c_0 - z_j)z^2 + \\cdots$\n\nSo $\\phi_j'(0) = 1$ and the coefficient of $z^2$ is $\\beta_{j,2} = -(c_0 - z_j) = z_j - c_0$.\n\n$\\phi_j$ is injective on $\\mathbb{D}$ (as argued above).\n\n$\\phi_j$ satisfies the hypotheses of the Koebe theorem (injective, $\\phi_j(0) = 0$, $\\phi_j'(0) = 1$).\n\nBy part (e), $|\\beta_{j,2}| \\leq 2$, i.e., $|z_j - c_0| \\leq 2$ for $j = 1, 2$.\n\nTherefore $|z_1 - z_2| \\leq |z_1 - c_0| + |z_2 - c_0| \\leq 2 + 2 = 4$. \u2713\n\nNow let me compile the full solution.\n\nOne thing I want to double-check: in part (e), when we say \"by part (c) applied to $1/g$\", we need $1/g$ to be injective on $0 < |z| < 1$. Since $g$ is injective on $\\mathbb{D}$ with $g(0) = 0$, $g$ maps $\\mathbb{D} \\setminus \\{0\\}$ injectively to $\\mathbb{C} \\setminus \\{0\\}$ (well, to its image minus 0). And $1/w$ is injective on $\\mathbb{C} \\setminus \\{0\\}$. So $1/g$ is injective on $\\mathbb{D} \\setminus \\{0\\}$. \u2713\n\nAlso, $1/g(z) = 1/z + d_0 + d_1 z + \\cdots$ has the form required by part (c). \u2713\n\nLet me also make sure the equality case in part (e) is correct. If $|a_2| = 2$, then $|d_1| = 1$, and by equality in the area theorem (part c), all higher coefficients must be 0. So $1/g(z) = 1/z + d_1 z$ with $|d_1| = 1$. Write $d_1 = -e^{i\\theta}$ (so that the final form matches). Then $1/g = 1/z - e^{i\\theta} z$, so $g = z/(1 - e^{i\\theta} z^2)$. Then $f(z^2) = g(z)^2 = z^2/(1 - e^{i\\theta} z^2)^2$, so $f(z) = z/(1 - e^{i\\theta} z)^2$. \u2713\n\nActually, let me be more careful about the equality case in the area theorem. Part (c) says $\\sum_{n=1}^{\\infty} n|c_n|^2 \\leq 1$. Equality holds iff the area of the complement is 0. For a function $h(z) = 1/z + c_0 + c_1 z + \\cdots$ injective on the punctured disk, if the complement has area 0, then by the open mapping theorem, the image must be $\\mathbb{C}$ minus a set of measure zero, which for a closed set means it's a single point or... Actually, the complement is compact, and if it has area 0, it must be a single point (or empty, but it can't be empty since $h$ maps to $\\infty$ at $z = 0$).\n\nActually, the standard result is that equality in the area theorem forces $h(z) = 1/z + c_1 z$ with $|c_1| = 1$ (and $c_0 = 0$, $c_n = 0$ for $n \\geq 2$). This is because the complement has area 0 and must be a point, and by the form of the Laurent expansion, this forces the specific form.\n\nMore precisely: if $\\sum n|c_n|^2 = 1$, then Area$(K) = 0$. Since $K$ is compact and connected (for small perturbations), and $h$ maps a neighborhood of 0 (minus 0) to the complement of $K$, and $h(z) \\sim 1/z$ near 0, the set $K$ must be a single point. If $K = \\{p\\}$, then $h$ maps $\\mathbb{D} \\setminus \\{0\\}$ to $\\mathbb{C} \\setminus \\{p\\}$, and $h(z) - p$ maps to $\\mathbb{C} \\setminus \\{0\\}$, so $1/(h(z) - p)$ maps to $\\mathbb{C} \\setminus \\{0\\}$... Actually this argument is getting circular. Let me just state the standard result.\n\nThe equality case in the area theorem: if $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \\cdots$ is injective on $0 < |z| < 1$ and $\\sum n|c_n|^2 = 1$, then $c_0 = 0$, $c_n = 0$ for $n \\geq 2$, and $|c_1| = 1$. This is a standard result (see e.g., Duren's \"Univalent Functions\").\n\nSo $h(z) = 1/z + c_1 z$ with $|c_1| = 1$. In our application, $h = 1/g$, so $1/g(z) = 1/z + c_1 z$, giving $g(z) = z/(1 + c_1 z^2)$.\n\nThen $f(z^2) = g(z)^2 = z^2/(1 + c_1 z^2)^2$, so $f(z) = z/(1 + c_1 z)^2$.\n\nWriting $c_1 = -e^{i\\theta}$: $f(z) = z/(1 - e^{i\\theta} z)^2$. \u2713\n\nNow let me write the complete solution.\n\nActually, one more thing to verify in part (d): we need to show $g$ is injective. Let me redo this.\n\n$g(z) = z\\psi(z^2)$ where $\\psi$ is holomorphic on $\\mathbb{D}$ with $\\psi^2 = f(\\cdot)/(\\cdot)$ and $\\psi(0) = 1$.\n\nSuppose $g(z_1) = g(z_2)$. Then $z_1\\psi(z_1^2) = z_2\\psi(z_2^2)$.\n\nSquaring: $z_1^2\\psi(z_1^2)^2 = z_2^2\\psi(z_2^2)^2$, i.e., $z_1^2 \\cdot f(z_1^2)/z_1^2 = z_2^2 \\cdot f(z_2^2)/z_2^2$, i.e., $f(z_1^2) = f(z_2^2)$.\n\nSince $f$ is injective: $z_1^2 = z_2^2$, so $z_1 = \\pm z_2$.\n\nCase 1: $z_1 = z_2$. Done.\nCase 2: $z_1 = -z_2 \\neq 0$. Then $g(z_1) = g(-z_1)$, i.e., $z_1\\psi(z_1^2) = -z_1\\psi(z_1^2)$ (since $(-z_1)^2 = z_1^2$). This gives $2z_1\\psi(z_1^2) = 0$. Since $z_1 \\neq 0$ and $\\psi(z_1^2) \\neq 0$ (because $\\psi^2(z_1^2) = f(z_1^2)/z_1^2$ and $f(z_1^2) \\neq 0$ since $f$ is injective and $f(0) = 0$ with $z_1^2 \\neq 0$), we get a contradiction.\n\nSo $g$ is injective. \u2713\n\nAlso, $g$ is odd: $g(-z) = -z\\psi(z^2) = -g(z)$. \u2713\n\nNow let me also think about whether $g$ maps $\\mathbb{D}$ to $\\mathbb{C}$ with $g(0) = 0$ and $g'(0) = 1$. Yes: $g(0) = 0 \\cdot \\psi(0) = 0$, and $g'(z) = \\psi(z^2) + z \\cdot 2z\\psi'(z^2)$, so $g'(0) = \\psi(0) = 1$. \u2713\n\nEverything checks out. Let me now write the final solution.",
    "format": "unknown",
    "index": 0
  }
]
```

---

## Raw Response (truncated)

```json
{
  "id": "gen-1789204100-bn7ve8V1o0LTKVbSrENa",
  "object": "chat.completion",
  "created": 1789204100,
  "model": "inclusionai/ling-3.0-flash-vl:free",
  "provider": "Novita",
  "system_fingerprint": null,
  "service_tier": null,
  "choices": [
    {
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop",
      "native_finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "# Koebe\u2013Bieberbach Radius Theorem: Complete Proof\n\n## Part (a): No uniform $r$ exists without further restrictions\n\n**Proof.** Define $f_n(z) = z/n$ for $n = 1, 2, 3, \\ldots$\n\nEach $f_n$ is holomorphic on $\\mathbb{D}$ with $f_n(0) = 0$, and\n$$f_n(\\mathbb{D}) = \\left\\{\\frac{z}{n} : |z| < 1\\right\\} = D_{1/n}(0).$$\nSince $|1/n| = 1/n$, the point $1/n$ lies on the boundary of this open disk, so $1/n \\notin f_n(\\mathbb{D})$.\n\nWe compute $f_n'(0) = 1/n \\to 0$. For any proposed $r > 0$, choose $n$ with $1/n < r$; then $1/n \\in D_r(0)$ but $1/n \\notin f_n(\\mathbb{D})$, so no such $r$ exists. $\\blacksquare$\n\n## Part (b): No uniform $r$ exists even with $f'(0) = 1$\n\n**Proof.** Define $f_\\epsilon(z) = \\epsilon(e^{z/\\epsilon} - 1)$ for $\\epsilon > 0$.\n\n- $f_\\epsilon(0) = \\epsilon(e^0 - 1) = 0$.\n- $f_\\epsilon'(z) = e^{z/\\epsilon}$, so $f_\\epsilon'(0) = 1$.\n- $f_\\epsilon$ is entire, hence holomorphic on $\\mathbb{D}$.\n\nSince $e^{z/\\epsilon} \\neq 0$ for all $z \\in \\mathbb{C}$, we have $f_\\epsilon(z) = \\epsilon(e^{z/\\epsilon} - 1) \\neq -\\epsilon$ for all $z$. Thus $-\\epsilon \\notin f_\\epsilon(\\mathbb{D})$.\n\nFor any $r > 0$, choose $\\epsilon < r$. Then $|-\\epsilon| = \\epsilon < r$, so $-\\epsilon \\in D_r(0)$, yet $-\\epsilon \\notin f_\\epsilon(\\mathbb{D})$. No uniform $r$ exists. $\\blacksquare$\n\n## Part (c): Area theorem \u2014 $\\sum_{n=1}^{\\infty} n|c_n|^2 \\leq 1$\n\n**Proof.** Let $h(z) = 1/z + c_0 + c_1 z + c_2 z^2 + \\cdots$ be injective on $0 < |z| < 1$. For $0 < \\rho < 1$, consider $h$ on the punctured disk $D_\\rho(0)\\setminus\\{0\\}$.\n\n**Step 1 (Change of variable).** Set $w = 1/z$ and define $G(w) = h(1/w) = w + c_0 + c_1/w + c_2/w^2 + \\cdots$, which is injective on $\\{|w| > 1/\\rho\\}$. As $z \\to 0$, $h(z) \\to \\infty$, so $h(D_\\rho(0)\\setminus\\{0\\})$ is unbounded with compact complement $K_\\rho$.\n\n**Step 2 (Area computation).** For $R > 1/\\rho$, compute the signed area enclosed by the Jordan curve $\\Gamma_R = G(\\{|w| = R\\})$ using:\n$$A(R) = \\frac{1}{2i}\\oint_{|w|=R} \\overline{G(w)}\\, G'(w)\\, dw.$$\n\nWriting $G(w) = \\sum_n a_n w^n$ (with $a_1 = 1$, $a_{-n} = c_n$), and using $\\bar{w} = R^2/w$ on $|w|=R$, the integrand $\\overline{G(w)}G'(w)$ has Laurent expansion whose $w^{-1}$ coefficient is $\\sum_n n|a_n|^2 R^{2n}$. By the residue theorem:\n$$A(R) = \\pi\\left(R^2 - \\sum_{n=1}^{\\infty} n|c_n|^2 R^{-2n}\\right).$$\n\n**Step 3 (Area of complement).** The enclosed area decomposes as $A(R) = \\text{Area}(K_\\rho) + \\text{Area}(G(\\{1/\\rho < |w| < R\\}))$. As $R \\to (1/\\rho)^+$, the annular contribution vanishes, giving:\n$$\\text{Area}(K_\\rho) = \\pi\\left(\\frac{1}{\\rho^2} - \\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n}\\right).$$\n\n**Step 4 (Conclusion).** Since Area$(K_\\rho) \\geq 0$, we get $\\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n} \\leq 1/\\rho^2$ for all $\\rho \\in (0,1)$. Letting $\\rho \\to 1^-$ (by monotone convergence):\n$$\\boxed{\\sum_{n=1}^{\\infty} n|c_n|^2 \\leq 1.} \\qquad \\blacksquare$$\n\n## Part (d): Existence of $g$ with $g^2(z) = f(z^2)$\n\n**Proof.** Let $f(z) = z + a_2 z^2 + \\cdots$ be injective on $\\mathbb{D}$ with $f(0) = 0$, $f'(0) = 1$.\n\n**Step 1 ($f(z)/z$ never vanishes).** Since $f(z) = z(1 + a_2 z + \\cdots)$, clearly $f(z)/z \\neq 0$ near 0. For $z \\neq 0$: if $f(z)/z = 0$ then $f(z) = 0 = f(0)$, contradicting injectivity. So $f(z)/z \\neq 0$ on all of $\\mathbb{D}$.\n\n**Step 2 (Holomorphic square root).** Since $\\mathbb{D}$ is simply connected and $f(z)/z$ is holomorphic and nowhere vanishing, there exists a holomorphic square root $\\psi$ on $\\mathbb{D}$ with $\\psi^2(z) = f(z)/z$ and $\\psi(0) = 1$.\n\n**Step 3 (Definition and properties of $g$).** Define $g(z) = z\\psi(z^2)$. Then:\n$$g(z)^2 = z^2\\psi(z^2)^2 = z^2 \\cdot \\frac{f(z^2)}{z^2} = f(z^2).$$\nAlso $g(0) = 0$ and $g'(0) = \\psi(0) = 1$.\n\n**Step 4 (Injectivity of $g$).** Suppose $g(z_1) = g(z_2)$. Squaring gives $f(z_1^2) = f(z_2^2)$, so by injectivity of $f$: $z_1^2 = z_2^2$, hence $z_1 = \\pm z_2$. If $z_1 = -z_2 \\neq 0$, then $g(z_1) = g(-z_1)$ gives $z_1\\psi(z_1^2) = -z_1\\psi(z_1^2)$ (using $g$ is odd since $g(-z) = -z\\psi(z^2) = -g(z)$). This forces $2z_1\\psi(z_1^2) = 0$. But $z_1 \\neq 0$ and $\\psi(z_1^2) \\neq 0$ (since $\\psi^2(z_1^2) = f(z_1^2)/z_1^2 \\neq 0$ because $f(z_1^2) \\neq 0$ by injectivity). Contradiction. Hence $z_1 = z_2$, and $g$ is injective. $\\blacksquare$\n\n## Part (e): $|a_2| \\leq 2$ with equality characterization\n\n**Proof.**\n\n**Step 1 (Structure of $g$).** From part (d), $g(z) = z\\psi(z^2)$ where $\\psi(z) = \\sqrt{f(z)/z}$. Writing $\\psi(z) = 1 + \\frac{a_2}{2}z + \\cdots$ (from $\\psi^2 = 1 + a_2 z + \\cdots$), we get:\n$$g(z) = z + \\frac{a_2}{2}z^3 + \\cdots$$\nwhich is an odd function with $g'(0) = 1$.\n\n**Step 2 (Apply area theorem to $1/g$).** Since $g$ is injective on $\\mathbb{D}$ with $g(0) = 0$, the function $1/g$ is injective on $\\mathbb{D}\\setminus\\{0\\}$ with a simple pole at 0:\n$$\\frac{1}{g(z)} = \\frac{1}{z} - \\frac{a_2}{2}z + \\cdots$$\n(using $g(z) = z(1 + \\frac{a_2}{2}z^2 + \\cdots)$, so $1/g = z^{-1}(1 - \\frac{a_2}{2}z^2 + \\cdots)$).\n\nThis has the form $1/z + d_0 + d_1 z + \\cdots$ with $d_1 = -a_2/2$. By part (c):\n$$|d_1|^2 \\leq \\sum_{n=1}^{\\infty} n|d_n|^2 \\leq 1 \\implies |d_1| \\leq 1.$$\n\n**Step 3 (Conclusion).** Since $d_1 = -a_2/2$:\n$$|a_2| = 2|d_1| \\leq 2.$$\n\n**Step 4 (Equality case).** If $|a_2| = 2$, then $|d_1| = 1$ and equality holds in $\\sum n|d_n|^2 \\leq 1$. By the area theorem equality case (Area$(K) = 0$ forces $1/g(z) = 1/z + e^{i\\theta}z$ for some $\\theta$), we get:\n$$g(z) = \\frac{z}{1 + e^{i\\theta}z^2}, \\quad f(z^2) = g(z)^2 = \\frac{z^2}{(1+e^{i\\theta}z^2)^2}.$$\nSubstituting $z^2 \\mapsto z$:\n$$\\boxed{f(z) = \\frac{z}{(1 - e^{i\\theta}z)^2}.} \\qquad \\blacksquare$$\n\n## Part (f): $|z_1 - z_2| \\leq 4$\n\n**Proof.** Let $h(z) = 1/z + c_0 + c_1 z + \\cdots$ be injective on $0 < |z| < 1$, avoiding values $z_1$ and $z_2$.\n\n**Step 1 (Construct normalized univalent functions).** For $j = 1, 2$, define $\\phi_j(z) = 1/(h(z) - z_j)$ on $\\mathbb{D}\\setminus\\{0\\}$. Since $h$ has a simple pole at 0:\n$$\\phi_j(z) = \\frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \\cdots} = z - (c_0 - z_j)z^2 + \\cdots$$\nextends holomorphically to $\\phi_j(0) = 0$ with $\\phi_j'(0) = 1$.\n\n**Step 2 (Injectivity).** Since $h$ is injective and $w \\mapsto 1/(w - z_j)$ is injective on $\\mathbb{C}\\setminus\\{z_j\\}$ (M\u00f6bius transformation), $\\phi_j$ is injective on $\\mathbb{D}\\setminus\\{0\\}$. Since $\\phi_j(z) \\neq 0 = \\phi_j(0)$ for $z \\neq 0$ (as $h(z) \\neq \\infty$ for $z \\neq 0$), $\\phi_j$ is injective on all of $\\mathbb{D}$.\n\n**Step 3 (Apply part (e)).** Each $\\phi_j$ satisfies $\\phi_j(0) = 0$, $\\phi_j'(0) = 1$, and is injective. The coefficient of $z^2$ in $\\phi_j$ is $\\beta_j = z_j - c_0$. By part (e):\n$$|z_j - c_0| = |\\beta_j| \\leq 2 \\quad \\text{for } j = 1, 2.$$\n\n**Step 4 (Triangle inequality).**\n$$\\boxed{|z_1 - z_2| \\leq |z_1 - c_0| + |c_0 - z_2| \\leq 2 + 2 = 4.} \\qquad \\blacksquare$$\n\n## Part (g): Completing the proof of the Koebe\u2013Bieberbach theorem\n\n**Theorem.** If $f: \\mathbb{D} \\to \\mathbb{C}$ is injective, holomorphic, with $f(0) = 0$ and $f'(0) = 1$, then $D_{1/4}(0) \\subseteq f(\\mathbb{D})$.\n\n**Proof.** Suppose for contradiction that some $w$ with $|w| < 1/4$ satisfies $w \\notin f(\\mathbb{D})$.\n\n**Step 1 (Construct an admissible $h$).** Define $h(z) = 1/f(z)$
```
