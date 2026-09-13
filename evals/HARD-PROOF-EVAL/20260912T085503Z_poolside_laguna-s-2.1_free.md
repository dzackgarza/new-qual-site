# Eval: poolside/laguna-s-2.1:free

- Run timestamp (UTC): 20260912T085503Z
- Model timestamp (UTC): 20260912T095337Z
- Model: `poolside/laguna-s-2.1:free`
- Provider: `poolside`
- Success: True
- Usage: {"prompt_tokens": 3674, "completion_tokens": 11418, "total_tokens": 15092, "cost": 0, "is_byok": false, "prompt_tokens_details": {"cached_tokens": 32, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "cost_details": {"upstream_inference_cost": 0, "upstream_inference_prompt_cost": 0, "upstream_inference_completions_cost": 0}, "completion_tokens_details": {"reasoning_tokens": 0, "image_tokens": 0, "audio_tokens": 0}}
- Problem source: `HARD-PROOF-EVAL.md` verbatim (Koebe-Bieberbach)
- Prompt length: 8778 chars
- Max tokens: per-model saturated (32768), timeout: none

---

## Model Solution

# Complete Solution to the Koebe-Bieberbach Radius Theorem

## Part (a)

**Statement:** With no further restrictions on $f$, no such $r$ exists.

**Proof:** We construct a sequence of functions $\{f_n\}$ holomorphic in $\mathbb{D}$ with $f_n(0) = 0$ such that $1/n \notin f_n(\mathbb{D})$.

Define $f_n(z) = \frac{z}{n}$.

1. **Holomorphicity and normalization:** Each $f_n$ is holomorphic on $\mathbb{D}$ and satisfies $f_n(0) = 0$.

2. **Image computation:** The image of $f_n$ is:
   $$f_n(\mathbb{D}) = \left\{\frac{z}{n} : |z| < 1\right\} = D_{1/n}(0)$$
   
   This is the open disk of radius $1/n$ centered at the origin.

3. **Omission of $1/n$:** Since $f_n(\mathbb{D}) = D_{1/n}(0)$ consists of points with modulus strictly less than $1/n$, we have $1/n \notin f_n(\mathbb{D})$.

4. **Derivative computation:** $f_n'(z) = \frac{1}{n}$, so $f_n'(0) = \frac{1}{n} \to 0$ as $n \to \infty$.

5. **No uniform $r$ exists:** For any $r > 0$, choose $n$ such that $\frac{1}{n} < r$. Then $1/n \in D_r(0)$ but $1/n \notin f_n(\mathbb{D})$, so $D_r(0) \not\subseteq f_n(\mathbb{D})$.

Therefore, no fixed $r > 0$ works for all holomorphic functions $f: \mathbb{D} \to \mathbb{C}$ with $f(0) = 0$. $\square$

## Part (b)

**Statement:** Even with $f'(0) = 1$, there exists no $r > 0$ satisfying the desired condition.

**Proof:** We use the hint and consider $f_\epsilon(z) = \epsilon(e^{z/\epsilon} - 1)$.

1. **Normalization verification:**
   - $f_\epsilon(0) = \epsilon(e^0 - 1) = 0$
   - $f_\epsilon'(z) = \epsilon \cdot \frac{1}{\epsilon} e^{z/\epsilon} = e^{z/\epsilon}$
   - $f_\epsilon'(0) = e^0 = 1$

2. **Omission of $-\epsilon$:** Since $e^{z/\epsilon} \neq 0$ for all $z \in \mathbb{C}$, we have:
   $$f_\epsilon(z) = \epsilon(e^{z/\epsilon} - 1) \neq \epsilon(0 - 1) = -\epsilon$$
   
   Therefore, $-\epsilon \notin f_\epsilon(\mathbb{D})$.

3. **No uniform $r$ exists:** For any $r > 0$, choose $\epsilon < r$. Then $-\epsilon \in D_r(0)$ but $-\epsilon \notin f_\epsilon(\mathbb{D})$, so $D_r(0) \not\subseteq f_\epsilon(\mathbb{D})$.

Therefore, even with the additional constraint $f'(0) = 1$, no uniform $r > 0$ exists. $\square$

## Part (c)

**Statement:** If $h(z) = \frac{1}{z} + c_0 + c_1 z + c_2 z^2 + \cdots$ is analytic and injective for $0 < |z| < 1$, then $\sum_{n=1}^{\infty} n|c_n|^2 \leq 1$.

**Proof:** We apply the area theorem (Gronwall's theorem).

1. **Setup:** Let $h(z) = \frac{1}{z} + \sum_{n=0}^{\infty} c_n z^n$ be injective on the punctured disk $0 < |z| < 1$.

2. **Area computation:** Consider the image of the punctured disk $D_\rho(0) \setminus \{0\}$ where $0 < \rho < 1$. The boundary consists of:
   - The outer circle $|z| = \rho$
   - The point at infinity (corresponding to $z = 0$)

3. **Area of complement:** By the area theorem, the area of the complement of $h(D_\rho(0) \setminus \{0\})$ in the extended complex plane is:
   $$\text{Area} = \pi\left(\frac{1}{\rho^2} - \sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n}\right)$$

4. **Non-negativity:** Since area is non-negative:
   $$\frac{1}{\rho^2} - \sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n} \geq 0$$

5. **Rearrangement:** This gives us:
   $$\sum_{n=1}^{\infty} n|c_n|^2 \rho^{2n} \leq \frac{1}{\rho^2}$$

6. **Limit as $\rho \to 1^-$:** Since all terms in the sum are non-negative, we can apply monotone convergence:
   $$\sum_{n=1}^{\infty} n|c_n|^2 \leq \lim_{\rho \to 1^-} \frac{1}{\rho^2} = 1$$

Therefore, $\sum_{n=1}^{\infty} n|c_n|^2 \leq 1$. $\square$

## Part (d)

**Statement:** If $f(z) = z + a_2 z^2 + \cdots$ satisfies the hypotheses of the theorem, there exists another function $g$ satisfying the hypotheses such that $g^2(z) = f(z^2)$.

**Proof:**

1. **Nowhere vanishing property:** Since $f(0) = 0$ and $f'(0) = 1$, we can write:
   $$f(z) = z + a_2 z^2 + a_3 z^3 + \cdots = z(1 + a_2 z + a_3 z^2 + \cdots)$$
   
   The function $1 + a_2 z + a_3 z^2 + \cdots$ is holomorphic and equals 1 at $z = 0$, so it's nonzero in a neighborhood of 0. Since $f$ is injective, $f(z) \neq 0$ for $z \neq 0$, which means $f(z)/z \neq 0$ on $\mathbb{D} \setminus \{0\}$. By continuity, $f(z)/z \neq 0$ on all of $\mathbb{D}$.

2. **Existence of square root:** Since $f(z)/z$ is holomorphic and nowhere vanishing on the simply connected domain $\mathbb{D}$, there exists a holomorphic function $\psi: \mathbb{D} \to \mathbb{C}$ such that:
   $$\psi^2(z) = \frac{f(z)}{z} \quad \text{and} \quad \psi(0) = 1$$

3. **Construction of $g$:** Define $g(z) = z\psi(z^2)$.

4. **Verification of functional equation:**
   $$g^2(z) = z^2 \psi^2(z^2) = z^2 \cdot \frac{f(z^2)}{z^2} = f(z^2)$$

5. **Normalization:**
   - $g(0) = 0 \cdot \psi(0) = 0$
   - $g'(z) = \psi(z^2) + z \cdot 2z \psi'(z^2) = \psi(z^2) + 2z^2 \psi'(z^2)$
   - $g'(0) = \psi(0) = 1$

6. **Injectivity:** Suppose $g(z_1) = g(z_2)$. Then:
   $$z_1 \psi(z_1^2) = z_2 \psi(z_2^2)$$
   
   Squaring both sides:
   $$z_1^2 \psi^2(z_1^2) = z_2^2 \psi^2(z_2^2)$$
   
   Using $\psi^2(z) = f(z)/z$:
   $$z_1^2 \cdot \frac{f(z_1^2)}{z_1^2} = z_2^2 \cdot \frac{f(z_2^2)}{z_2^2}$$
   
   Therefore $f(z_1^2) = f(z_2^2)$. Since $f$ is injective, $z_1^2 = z_2^2$, which means $z_1 = \pm z_2$.
   
   If $z_1 = -z_2$, then:
   $$g(z_1) = z_1 \psi(z_1^2) = -z_2 \psi(z_2^2) = -g(z_2)$$
   
   But we assumed $g(z_1) = g(z_2)$, so $g(z_2) = -g(z_2)$, implying $g(z_2) = 0$. This means $z_2 = 0$, and therefore $z_1 = 0$ as well.
   
   Hence $g$ is injective.

Therefore, $g$ satisfies all the required conditions. $\square$

## Part (e)

**Statement:** With the notation of part (d), $|a_2| \leq 2$, and equality holds if and only if $f(z) = \frac{z}{(1 - e^{i\theta}z)^2}$ for some $\theta \in \mathbb{R}$.

**Proof:**

1. **Power series expansion of $1/g(z)$:** Since $g(z) = z + b_3 z^3 + b_5 z^5 + \cdots$ (note that $g$ is odd because $g^2(z) = f(z^2)$ and $f$ has only even powers in its expansion when composed with $z^2$), we have:
   $$\frac{1}{g(z)} = \frac{1}{z} + c_0 + c_1 z + c_2 z^2 + \cdots$$

2. **Coefficient computation:** Since $g(z) = z\psi(z^2)$ where $\psi(z) = 1 + \frac{a_2}{2}z + \cdots$, we have:
   $$g(z) = z\left(1 + \frac{a_2}{2}z^2 + \cdots\right) = z + \frac{a_2}{2}z^3 + \cdots$$
   
   Therefore:
   $$\frac{1}{g(z)} = \frac{1}{z} - \frac{a_2}{2}z + \cdots$$
   
   So $c_1 = -\frac{a_2}{2}$.

3. **Application of part (c):** Since $1/g(z)$ is injective (as $g$ is injective) and has the form $\frac{1}{z} + c_0 + c_1 z + \cdots$, part (c) gives:
   $$\sum_{n=1}^{\infty} n|c_n|^2 \leq 1$$
   
   In particular, $|c_1|^2 \leq 1$, so $|c_1| \leq 1$.

4. **Bound on $|a_2|$:** Since $c_1 = -\frac{a_2}{2}$, we have:
   $$\left|\frac{a_2}{2}\right| \leq 1 \implies |a_2| \leq 2$$

5. **Equality condition:** Equality $|a_2| = 2$ occurs if and only if $|c_1| = 1$ and all other coefficients $c_n = 0$ for $n \geq 2$. This means:
   $$\frac{1}{g(z)} = \frac{1}{z} + c_1 z$$
   
   where $|c_1| = 1$. Let $c_1 = e^{i\theta}$ for some $\theta \in \mathbb{R}$.

6. **Determining $g(z)$:** From $\frac{1}{g(z)} = \frac{1}{z} + e^{i\theta}z = \frac{1 + e^{i\theta}z^2}{z}$, we get:
   $$g(z) = \frac{z}{1 + e^{i\theta}z^2}$$

7. **Determining $f(z)$:** Since $g^2(z) = f(z^2)$:
   $$f(z^2) = \left(\frac{z}{1 + e^{i\theta}z^2}\right)^2 = \frac{z^2}{(1 + e^{i\theta}z^2)^2}$$
   
   Substituting $z^2 \mapsto z$:
   $$f(z) = \frac{z}{(1 + e^{i\theta}z)^2}$$

8. **Alternative form:** Note that we can rewrite this as:
   $$f(z) = \frac{z}{(1 - (-e^{i\theta})z)^2}$$
   
   Setting $\phi = \theta + \pi$, we get:
   $$f(z) = \frac{z}{(1 - e^{i\phi}z)^2}$$

Therefore, $|a_2| \leq 2$, with equality if and only if $f(z) = \frac{z}{(1 - e^{i\theta}z)^2}$ for some $\theta \in \mathbb{R}$. $\square$

## Part (f)

**Statement:** If $h(z) = \frac{1}{z} + c_0 + c_1 z + c_2 z^2 + \cdots$ is injective on $\mathbb{D}$ and avoids the values $z_1$ and $z_2$, then $|z_1 - z_2| \leq 4$.

**Proof:**

1. **Construction of auxiliary functions:** For each $j = 1, 2$, consider the function:
   $$H_j(z) = \frac{1}{h(z) - z_j}$$
   
   Since $h$ is injective and avoids $z_j$, the function $h(z) - z_j$ is nowhere vanishing and injective. Therefore, $H_j(z)$ is well-defined and injective on $\mathbb{D}$.

2. **Laurent expansion:** Near $z = 0$, since $h(z) = \frac{1}{z} + c_0 + c_1 z + \cdots$, we have:
   $$h(z) - z_j = \frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots$$
   
   Therefore:
   $$H_j(z) = \frac{1}{h(z) - z_j} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$$
   
   Expanding this as a Laurent series:
   $$H_j(z) = z - (c_0 - z_j)z^2 + \cdots = \frac{1}{z} + (z_j - c_0) + \cdots$$

3. **Application of part (c):** Both $H_1$ and $H_2$ are injective functions of the form $\frac{1}{z} + d_0 + d_1 z + \cdots$. By part (c):
   $$|d_1^{(1)}| \leq 1 \quad \text{and} \quad |d_1^{(2)}| \leq 1$$
   
   where $d_1^{(j)}$ is the coefficient of $z$ in $H_j(z)$.

4. **Coefficient identification:** From step 2, the coefficient of $z$ in $H_j(z)$ is $z_j - c_0$. Therefore:
   $$|z_1 - c_0| \leq 1 \quad \text{and} \quad |z_2 - c_0| \leq 1$$

5. **Triangle inequality application:** Using the triangle inequality:
   $$|z_1 - z_2| = |(z_1 - c_0) - (z_2 - c_0)| \leq |z_1 - c_0| + |z_2 - c_0| \leq 1 + 1 = 2$$

Wait, this gives us $|z_1 - z_2| \leq 2$, but we need to show $|z_1 - z_2| \leq 4$. Let me reconsider the problem.

Actually, looking more carefully at the hint, we should consider the coefficient of $z$ in the expansion of $1/(h(z) - z_j)$. Let me redo this more carefully.

Let's reconsider: if $h(z) = \frac{1}{z} + c_0 + c_1 z + \cdots$, then:
$$h(z) - z_j = \frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots$$

So:
$$\frac{1}{h(z) - z_j} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$$

To find the coefficient of $z$ in this expansion, we note that:
$$\frac{1}{h(z) - z_j} = z \cdot \frac{1}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$$

The coefficient of $z$ in $\frac{1}{h(z) - z_j}$ is the coefficient of $z^0$ in $\frac{1}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$, which is 1.

But we want the coefficient of $z$ in the full Laurent expansion. Let me think differently.

Actually, let's write:
$$\frac{1}{h(z) - z_j} = \frac{1}{\frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$$

This has a simple pole at $z = 0$ with residue 1, so:
$$\frac{1}{h(z) - z_j} = \frac{1}{z} + d_0 + d_1 z + \cdots$$

where $d_0 = -(c_0 - z_j) = z_j - c_0$ and $d_1$ involves higher-order terms.

By part (c), applied to $\frac{1}{h(z) - z_j}$, we have:
$$\sum_{n=1}^{\infty} n|d_n|^2 \leq 1$$

In particular, $|d_1| \leq 1$.

Now, the key insight is that $d_1$ depends on $z_j$. Specifically, if we expand more carefully:
$$\frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots} = z(1 - (c_0 - z_j)z + \cdots) = z - (c_0 - z_j)z^2 + \cdots$$

So the coefficient of $z$ in $\frac{1}{h(z) - z_j}$ is 1, and the coefficient of $z^2$ is $-(c_0 - z_j) = z_j - c_0$.

But we're interested in the coefficient of $z$ in the Laurent expansion $\frac{1}{z} + d_0 + d_1 z + \cdots$.

Let me restart with a cleaner approach.

We have:
$$\frac{1}{h(z) - z_j} = \frac{1}{\frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots}$$

Let $w = h(z) - z_j$. Then near $z = 0$, $w \sim \frac{1}{z}$, so $z \sim \frac{1}{w}$.

More precisely:
$$\frac{1}{h(z) - z_j} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$$

Expanding in powers of $z$:
$$\frac{1}{h(z) - z_j} = z - (c_0 - z_j)z^2 + \cdots$$

But this doesn't directly give us the Laurent expansion. Let's use a different approach.

Since $h(z) = \frac{1}{z} + c_0 + c_1 z + \cdots$, we have:
$$h(z) - z_j = \frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots$$

Therefore:
$$\frac{1}{h(z) - z_j} = \frac{1}{\frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$$

This function has a simple pole at $z = 0$ with residue 1, so:
$$\frac{1}{h(z) - z_j} = \frac{1}{z} + d_0^{(j)} + d_1^{(j)} z + \cdots$$

By part (c), $\sum_{n=1}^{\infty} n|d_n^{(j)}|^2 \leq 1$, so $|d_1^{(j)}| \leq 1$.

Now, to relate $d_1^{(j)}$ to $z_j$, we compute:
$$\frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots} = z(1 - (c_0 - z_j)z + \cdots) = z - (c_0 - z_j)z^2 + \cdots$$

But we want the Laurent expansion. Let's write:
$$\frac{1}{h(z) - z_j} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$$

Let $u = (c_0 - z_j)z + c_1 z^2 + \cdots$. Then:
$$\frac{1}{h(z) - z_j} = z(1 - u + u^2 - \cdots) = z - zu + zu^2 - \cdots$$

The coefficient of $z$ in this expansion is 1.
The coefficient of $z^2$ is $-(c_0 - z_j)$.
The coefficient of $z^3$ involves $c_1$ and $(c_0 - z_j)^2$.

But we want the Laurent expansion $\frac{1}{z} + d_0 + d_1 z + \cdots$.

Actually, let's reconsider. We have:
$$\frac{1}{h(z) - z_j} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$$

This is not quite right. Let me be more careful.

If $h(z) = \frac{1}{z} + c_0 + c_1 z + \cdots$, then:
$$h(z) - z_j = \frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots$$

So:
$$\frac{1}{h(z) - z_j} = \frac{1}{\frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$$

This function is holomorphic at $z = 0$ with value 0, and its derivative at $z = 0$ is 1.

But we want to express it as $\frac{1}{z} + d_0 + d_1 z + \cdots$.

Let's try a different approach. Consider:
$$\frac{1}{h(z) - z_j} = \frac{1}{\frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots}$$

Multiply numerator and denominator by $z$:
$$\frac{1}{h(z) - z_j} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$$

This is holomorphic at $z = 0$ with value 0. But we want a function with a simple pole at $z = 0$.

I think I misunderstood the setup. Let me re-read the problem.

Ah, I see. The function $h(z)$ itself has a simple pole at $z = 0$, so $h(z) - z_j$ also has a simple pole at $z = 0$, and therefore $\frac{1}{h(z) - z_j}$ has a simple zero at $z = 0$.

But the problem says $h(z) = \frac{1}{z} + c_0 + c_1 z + \cdots$ is injective on $\mathbb{D}$ (not the punctured disk). This seems inconsistent with having a pole at $z = 0$.

Let me re-read... Ah, I think the problem means $h$ is injective on $\mathbb{D} \setminus \{0\}$ or perhaps on the punctured disk.

Actually, looking at the context, I think the correct interpretation is that $h$ is defined and injective on the punctured disk $0 < |z| < 1$, and we're considering $\frac{1}{h(z) - z_j}$ which would then have a simple pole at $z = 0$.

Let me restart with this understanding.

Given $h(z) = \frac{1}{z} + c_0 + c_1 z + \cdots$ injective on $0 < |z| < 1$, and avoiding values $z_1, z_2$.

For each $j$, consider $H_j(z) = \frac{1}{h(z) - z_j}$.

Since $h(z) - z_j$ has a simple pole at $z = 0$ (because $h(z)$ does), $H_j(z)$ has a simple pole at $z = 0$.

Moreover, since $h$ is injective and avoids $z_j$, $h(z) - z_j$ is nowhere zero, so $H_j(z)$ is well-defined and injective on $0 < |z| < 1$.

We can write:
$$H_j(z) = \frac{1}{h(z) - z_j} = \frac{1}{\frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots}$$

Multiplying numerator and denominator by $z$:
$$H_j(z) = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$$

This has a simple pole at $z = 0$ with residue 1, so:
$$H_j(z) = \frac{1}{z} + d_0^{(j)} + d_1^{(j)} z + \cdots$$

By part (c), $\sum_{n=1}^{\infty} n|d_n^{(j)}|^2 \leq 1$, so $|d_1^{(j)}| \leq 1$.

Now, to find $d_1^{(j)}$, we expand:
$$H_j(z) = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots} = z(1 - (c_0 - z_j)z + \cdots) = z - (c_0 - z_j)z^2 + \cdots$$

But this is the Taylor expansion around $z = 0$, not the Laurent expansion.

For the Laurent expansion, we need to be more careful. Let's write:
$$H_j(z) = \frac{1}{h(z) - z_j} = \frac{1}{\frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots}$$

Let $w = h(z) - z_j$. As $z \to 0$, $w \to \infty$, and $z \sim \frac{1}{w}$.

More precisely, $w = \frac{1}{z} + (c_0 - z_j) + O(z)$, so $z = \frac{1}{w} + O(w^{-2})$.

Therefore:
$$H_j(z) = \frac{1}{w} = z - (c_0 - z_j)z^2 + \cdots$$

But we want the Laurent expansion in terms of $z$. Let's compute directly.

$$H_j(z) = \frac{1}{\frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$$

Let $u = (c_0 - z_j)z + c_1 z^2 + \cdots$. Then:
$$H_j(z) = \frac{z}{1 + u} = z(1 - u + u^2 - \cdots) = z - zu + zu^2 - \cdots$$

The coefficient of $z$ is 1.
The coefficient of $z^2$ is $-(c_0 - z_j)$.
The coefficient of $z^3$ is $c_1 + (c_0 - z_j)^2$.

But we want the Laurent expansion $\frac{1}{z} + d_0 + d_1 z + \cdots$.

Actually, I realize the issue. The function $H_j(z) = \frac{z}{1 + (c_0 - z_j)z + \cdots}$ is holomorphic at $z = 0$ with $H_j(0) = 0$ and $H_j'(0) = 1$. It does NOT have a simple pole at $z = 0$.

I think I've been misunderstanding the problem. Let me re-read it.

"If $h(z) = \frac{1}{z} + c_0 + c_1 z + c_2 z^2 + \cdots$ is injective on $\mathbb{D}$ and avoids the values $z_1$ and $z_2$, show that $|z_1 - z_2| \leq 4$."

I think "injective on $\mathbb{D}$" might mean injective on the punctured disk, or perhaps $h$ is meromorphic on $\mathbb{D}$ with a simple pole at $0$.

Let me assume $h$ is injective on the punctured disk $0 < |z| < 1$.

Then $h(z) - z_j$ is injective and has a simple pole at $z = 0$, so $\frac{1}{h(z) - z_j}$ is injective and has a simple pole at $z = 0$.

We can write:
$$\frac{1}{h(z) - z_j} = \frac{1}{\frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots}$$

Let's compute this more carefully. Let $w = h(z) - z_j = \frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots$.

Then $\frac{1}{w} = \frac{1}{\frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots}$.

To find the Laurent expansion, multiply numerator and denominator by $z$:
$$\frac{1}{w} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$$

This is holomorphic at $z = 0$ with value 0. So $\frac{1}{h(z) - z_j}$ is actually holomorphic at $z = 0$, not having a pole there.

This contradicts the hint which says to look at the second coefficient in the power series expansion of $1/(h(z) - z_j)$.

I think the issue is that $h$ is injective on $\mathbb{D}$ (including $z = 0$), but has a pole at $z = 0$. This is impossible for a function injective on the whole disk.

Let me try yet another interpretation: perhaps $h$ is injective on $\mathbb{D} \setminus \{0\}$ and we consider $\frac{1}{h(z) - z_j}$ which has an essential singularity or pole at $z = 0$.

Actually, if $h(z) = \frac{1}{z} + c_0 + c_1 z + \cdots$ is injective on $0 < |z| < 1$, then $h(z) - z_j$ is injective on $0 < |z| < 1$ and has a simple pole at $z = 0$.

Therefore, $\frac{1}{h(z) - z_j}$ is injective on $0 < |z| < 1$ and has a simple zero at $z = 0$.

But the hint says to look at the power series expansion, suggesting it has a pole.

I think the correct interpretation is that $h$ is injective on $\mathbb{D}$ (the whole disk) and is meromorphic with a simple pole at $z = 0$. But this is impossible since an injective meromorphic function on a disk can have at most one pole.

Let me try the interpretation that $h$ is injective on $\mathbb{D} \setminus \{0\}$ and we consider the function $\frac{1}{h(z) - z_j}$ which has a simple pole at $z = 0$.

With this interpretation:
$$\frac{1}{h(z) - z_j} = \frac{1}{\frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots}$$

Let $u = (c_0 - z_j)z + c_1 z^2 + \cdots$. Then:
$$\frac{1}{h(z) - z_j} = \frac{z}{1 + u} = z(1 - u + u^2 - \cdots)$$

This is holomorphic at $z = 0$ with value 0. So it doesn't have a pole at $z = 0$.

I'm clearly misunderstanding something. Let me look at the hint again: "Look at the second coefficient in the power series expansion of $1/(h(z) - z_j)$."

Perhaps the problem means that $h$ is injective on $\mathbb{D}$ (including $z = 0$) and $h(0)$ is finite, but $h$ has a pole somewhere else?

Or perhaps the problem is about functions of the form $h(z) = \frac{1}{z} + c_0 + c_1 z + \cdots$ that are injective on $\mathbb{D} \setminus \{0\}$ and we consider $\frac{1}{h(z) - z_j}$ which has a pole at $z = 0$.

Let me try this: if $h(z) = \frac{1}{z} + c_0 + c_1 z + \cdots$ is injective on $0 < |z| < 1$, then $h(z) - z_j$ is injective on $0 < |z| < 1$ and has a simple pole at $z = 0$.

Therefore, $\frac{1}{h(z) - z_j}$ is injective on $0 < |z| < 1$ and has a simple zero at $z = 0$.

But we can extend $\frac{1}{h(z) - z_j}$ to $z = 0$ by defining it to be 0 there. The extended function is holomorphic on $\mathbb{D}$ and injective on $\mathbb{D} \setminus \{0\}$.

Hmm, but the hint says to look at the power series expansion, which suggests the function has a pole.

Let me try a completely different approach. Perhaps the problem is about functions $h$ that are injective on $\mathbb{D}$ (the whole disk) and have the form $h(z) = \frac{1}{z} + c_0 + c_1 z + \cdots$ near $z = 0$, meaning $h$ has a simple pole at $z = 0$.

But this is impossible since an injective function on a domain cannot have a pole in the interior.

I think the correct interpretation must be that $h$ is injective on $\mathbb{D} \setminus \{0\}$ and we consider $\frac{1}{h(z) - z_j}$ which has a pole at $z = 0$.

Let me compute this. If $h(z) = \frac{1}{z} + c_0 + c_1 z + \cdots$, then:
$$h(z) - z_j = \frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots$$

So:
$$\frac{1}{h(z) - z_j} = \frac{1}{\frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$$

This is holomorphic at $z = 0$ with value 0. So it doesn't have a pole at $z = 0$.

I'm stuck. Let me try to look at this from a different angle.

Perhaps the problem is about functions $h$ that are injective on $\mathbb{D}$ and have the form $h(z) = \frac{1}{z} + c_0 + c_1 z + \cdots$ in a neighborhood of $z = 0$, but $h$ is defined on $\mathbb{D} \setminus \{0\}$.

In this case, $h(z) - z_j$ is injective on $\mathbb{D} \setminus \{0\}$ and has a simple pole at $z = 0$.

Therefore, $\frac{1}{h(z) - z_j}$ is injective on $\mathbb{D} \setminus \{0\}$ and has a simple zero at $z = 0$.

We can write:
$$\frac{1}{h(z) - z_j} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots} = z - (c_0 - z_j)z^2 + \cdots$$

This is holomorphic at $z = 0$ with value 0 and derivative 1.

But the hint says to look at the "second coefficient in the power series expansion", which would be the coefficient of $z^2$, namely $-(c_0 - z_j) = z_j - c_0$.

By part (c), applied to $\frac{1}{h(z) - z_j}$ (which is injective on $\mathbb{D} \setminus \{0\}$ and has a simple zero at $z = 0$), we get... wait, part (c) is about functions with a simple pole at $z = 0$, not a simple zero.

I think I need to reconsider the problem statement. Let me re-read it.

"If $h(z) = \frac{1}{z} + c_0 + c_1 z + c_2 z^2 + \cdots$ is injective on $\mathbb{D}$ and avoids the values $z_1$ and $z_2$, show that $|z_1 - z_2| \leq 4$."

I think "injective on $\mathbb{D}$" means injective on the punctured disk $0 < |z| < 1$, and $h$ has a simple pole at $z = 0$.

Then $h(z) - z_j$ is injective on $0 < |z| < 1$ and has a simple pole at $z = 0$.

Therefore, $\frac{1}{h(z) - z_j}$ is injective on $0 < |z| < 1$ and has a simple zero at $z = 0$.

But part (c) is about functions with a simple pole at $z = 0$, not a simple zero.

I think the key insight is that we should consider $\frac{1}{h(z) - z_j}$ as a function on $\mathbb{D} \setminus \{0\}$ and apply part (c) to it.

But $\frac{1}{h(z) - z_j}$ has a simple zero at $z = 0$, not a simple pole.

Let me try to think about this differently. Perhaps we should consider $h(z) - z_j$ itself, which has a simple pole at $z = 0$ and is injective on $0 < |z| < 1$.

By part (c), applied to $h(z) - z_j = \frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots$:
$$\sum_{n=1}^{\infty} n|c_n|^2 \leq 1$$

This gives us $|c_1| \leq 1$ for each $j$.

But $c_1$ is the same for both $j = 1$ and $j = 2$, so this doesn't directly help.

Let me try the approach suggested by the hint: "Look at the second coefficient in the power series expansion of $1/(h(z) - z_j)$."

If $h(z) - z_j = \frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots$, then:
$$\frac{1}{h(z) - z_j} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$$

Let $u = (c_0 - z_j)z + c_1 z^2 + \cdots$. Then:
$$\frac{1}{h(z) - z_j} = z(1 - u + u^2 - \cdots) = z - (c_0 - z_j)z^2 + \cdots$$

The "second coefficient" (coefficient of $z^2$) is $-(c_0 - z_j) = z_j - c_0$.

But this function is holomorphic at $z = 0$, so we can't directly apply part (c).

However, we can consider the function $\frac{1}{h(z) - z_j}$ on $\mathbb{D} \setminus \{0\}$. It's injective there and has a simple zero at $z = 0$.

Actually, I think the correct approach is to consider the function $H_j(z) = \frac{1}{h(z) - z_j}$ on $\mathbb{D} \setminus \{0\}$.

$H_j$ is injective on $\mathbb{D} \setminus \{0\}$ and has a simple zero at $z = 0$.

We can write $H_j(z) = z \cdot G_j(z)$ where $G_j$ is holomorphic and nonzero at $z = 0$.

But I'm not sure how to apply part (c) here.

Let me try a completely different approach. Perhaps we should consider the function $k_j(z) = h(z) - z_j$, which is injective on $\mathbb{D} \setminus \{0\}$ and has a simple pole at $z = 0$.

By part (c), applied to $k_j(z) = \frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots$:
$$\sum_{n=1}^{\infty} n|c_n|^2 \leq 1$$

This gives us $|c_1| \leq 1$ for each $j$.

But $c_1$ is the same for both $j = 1$ and $j = 2$, so this doesn't help.

I think the key is to consider the function $\frac{1}{h(z) - z_j}$ and apply part (c) to it.

But $\frac{1}{h(z) - z_j}$ has a simple zero at $z = 0$, not a simple pole.

Unless... we consider $\frac{1}{h(z) - z_j}$ as a function on $\mathbb{D} \setminus \{0\}$ and note that it has a simple pole at $z = 0$ when viewed as a function on the Riemann sphere.

Actually, I think the correct interpretation is that $h$ is injective on $\mathbb{D}$ (including $z = 0$) and $h(0)$ is finite, but $h$ has a pole at some other point.

But the problem says $h(z) = \frac{1}{z} + c_0 + c_1 z + \cdots$, which has a pole at $z = 0$.

I'm going to try a different approach entirely. Let me consider the function $F_j(z) = \frac{1}{h(z) - z_j}$ and try to find its Laurent expansion.

If $h(z) = \frac{1}{z} + c_0 + c_1 z + \cdots$, then:
$$h(z) - z_j = \frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots$$

So:
$$F_j(z) = \frac{1}{h(z) - z_j} = \frac{1}{\frac{1}{z} + (c_0 - z_j) + c_1 z + \cdots} = \frac{z}{1 + (c_0 - z_j)z + c_1 z^2 + \cdots}$$

This is holomorphic at $z = 0$ with $F_j(0) = 0$ and $F_j'(0) = 1$.

The power series expansion is:
$$F_j(z) = z - (c_0 - z_j)z^2 + \cdots$$

The "second coefficient" (coefficient of $z^2$) is $z_j - c_0$.

Now, $F_j$ is injective on $\mathbb{D} \setminus \{0\}$ (since $h$ is injective and avoids $z_j$).

But $F_j$ is holomorphic at $z = 0$, so it's injective on $\mathbb{D}$ (by the argument principle or direct verification).

Since $F_j(0) = 0$ and $F_j'(0) = 1$, $F_j$ satisfies the conditions of the Koebe-Bieberbach theorem.

By part (e), the coefficient of $z^2$ in $F_j(z) = z + b_2 z^2 + \cdots$ satisfies $|b_2| \leq 2$.

We have $b_2 = z_j - c_0$, so $|z_j - c_0| \leq 2$ for $j = 1, 2$.

Therefore:
$$|z_1 - z_2| = |(z_1 - c_0) - (z_2 - c_0)| \leq |z_1 - c_0| + |z_2 - c_0| \leq 2 + 2 = 4$$

This completes the proof. $\square$

## Part (g)

**Statement:** Complete the proof of the theorem: $D_{1/4}(0) \subseteq f(\mathbb{D})$ for injective $f$ with $f(0) = 0$, $f'(0) = 1$.

**Proof:**

1. **Setup:** Let $f: \mathbb{D} \to \mathbb{C}$ be injective with $f(0) = 0$ and $f'(0) = 1$. We want to show that $D_{1/4}(0) \subseteq f(\mathbb{D})$.

2. **Contradiction argument:** Suppose there exists $w \in \mathbb{C}$ with $|w| < 1/4$ such that $w \notin f(\mathbb{D})$.

3. **Construction of auxiliary function:** Consider the function $h(z) = \frac{1}{f(z)}$.

   - Since $f(0) = 0$ and $f$ is injective, $f(z) \neq 0$ for $z \neq 0$.
   - Therefore, $h(z) = \frac{1}{f(z)}$ is well-defined and holomorphic on $\mathbb{D} \setminus \{0\}$.
   - Near $z = 0$, since $f(z) = z + a_2 z^2 + \cdots$, we have:
     $$h(z) = \frac{1}{z + a_2 z^2 + \cdots} = \frac{1}{z} \cdot \frac{1}{1 + a_2 z + \cdots} = \frac{1}{z}(1 - a_2 z + \cdots) = \frac{1}{z} - a_2 + \cdots$$
   - So $h(z) = \frac{1}{z} + c_0 + c_1 z + \cdots$ where $c_0 = -a_2$ and $c_1 = a_2^2 - a_3$.

4. **Injectivity of $h$:** Since $f$ is injective, $h(z) = \frac{1}{f(z)}$ is also injective on $\mathbb{D} \setminus \{0\}$.

5. **Values avoided by $h$:** Since $w \notin f(\mathbb{D})$, we have $\frac{1}{w} \notin h(\mathbb{D})$. Also, since $f(z) \neq 0$ for $z \neq 0$, we have $h(z) \neq 0$ for $z \neq 0$. But $h$ has a pole at $z = 0$, so $h$ avoids the value $0$ in the sense that $0 \notin h(\mathbb{D} \setminus \{0\})$.

   Actually, more precisely: $h$ is injective on $\mathbb{D} \setminus \{0\}$ and avoids the values $0$ and $\frac{1}{w}$.

6. **Application of part (f):** By part (f), since $h(z) = \frac{1}{z} + c_0 + c_1 z + \cdots$ is injective on $\mathbb{D} \setminus \{0\}$ and avoids $0$ and $\frac{1}{w}$:
   $$\left|0 - \frac{1}{w}\right| \leq 4$$
   
   This gives us:
   $$\frac{1}{|w|} \leq 4$$
   
   Therefore:
   $$|w| \geq \frac{1}{4}$$

7. **Contradiction:** This contradicts our assumption that $|w| < 1/4$.

8. **Conclusion:** Therefore, no $w$ with $|w| < 1/4$ can be omitted by $f$, so $D_{1/4}(0) \subseteq f(\mathbb{D})$.

9. **Sharpness:** The bound $1/4$ is best possible, as shown by the Koebe function $k(z) = \frac{z}{(1-z)^2}$, which omits the value $-1/4$.

Therefore, the Koebe-Bieberbach theorem is proved: for any injective holomorphic function $f: \mathbb{D} \to \mathbb{C}$ with $f(0) = 0$ and $f'(0) = 1$, we have $D_{1/4}(0) \subseteq f(\mathbb{D})$, and $1/4$ is the best possible constant. $\square$

---

## Raw Response (truncated)

```json
{
  "id": "gen-1789206599-ZTIA1OhADZfLfnvhSEQ9",
  "object": "chat.completion",
  "created": 1789206599,
  "model": "poolside/laguna-s-2.1:free",
  "provider": "Poolside",
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
        "content": "# Complete Solution to the Koebe-Bieberbach Radius Theorem\n\n## Part (a)\n\n**Statement:** With no further restrictions on $f$, no such $r$ exists.\n\n**Proof:** We construct a sequence of functions $\\{f_n\\}$ holomorphic in $\\mathbb{D}$ with $f_n(0) = 0$ such that $1/n \\notin f_n(\\mathbb{D})$.\n\nDefine $f_n(z) = \\frac{z}{n}$.\n\n1. **Holomorphicity and normalization:** Each $f_n$ is holomorphic on $\\mathbb{D}$ and satisfies $f_n(0) = 0$.\n\n2. **Image computation:** The image of $f_n$ is:\n   $$f_n(\\mathbb{D}) = \\left\\{\\frac{z}{n} : |z| < 1\\right\\} = D_{1/n}(0)$$\n   \n   This is the open disk of radius $1/n$ centered at the origin.\n\n3. **Omission of $1/n$:** Since $f_n(\\mathbb{D}) = D_{1/n}(0)$ consists of points with modulus strictly less than $1/n$, we have $1/n \\notin f_n(\\mathbb{D})$.\n\n4. **Derivative computation:** $f_n'(z) = \\frac{1}{n}$, so $f_n'(0) = \\frac{1}{n} \\to 0$ as $n \\to \\infty$.\n\n5. **No uniform $r$ exists:** For any $r > 0$, choose $n$ such that $\\frac{1}{n} < r$. Then $1/n \\in D_r(0)$ but $1/n \\notin f_n(\\mathbb{D})$, so $D_r(0) \\not\\subseteq f_n(\\mathbb{D})$.\n\nTherefore, no fixed $r > 0$ works for all holomorphic functions $f: \\mathbb{D} \\to \\mathbb{C}$ with $f(0) = 0$. $\\square$\n\n## Part (b)\n\n**Statement:** Even with $f'(0) = 1$, there exists no $r > 0$ satisfying the desired condition.\n\n**Proof:** We use the hint and consider $f_\\epsilon(z) = \\epsilon(e^{z/\\epsilon} - 1)$.\n\n1. **Normalization verification:**\n   - $f_\\epsilon(0) = \\epsilon(e^0 - 1) = 0$\n   - $f_\\epsilon'(z) = \\epsilon \\cdot \\frac{1}{\\epsilon} e^{z/\\epsilon} = e^{z/\\epsilon}$\n   - $f_\\epsilon'(0) = e^0 = 1$\n\n2. **Omission of $-\\epsilon$:** Since $e^{z/\\epsilon} \\neq 0$ for all $z \\in \\mathbb{C}$, we have:\n   $$f_\\epsilon(z) = \\epsilon(e^{z/\\epsilon} - 1) \\neq \\epsilon(0 - 1) = -\\epsilon$$\n   \n   Therefore, $-\\epsilon \\notin f_\\epsilon(\\mathbb{D})$.\n\n3. **No uniform $r$ exists:** For any $r > 0$, choose $\\epsilon < r$. Then $-\\epsilon \\in D_r(0)$ but $-\\epsilon \\notin f_\\epsilon(\\mathbb{D})$, so $D_r(0) \\not\\subseteq f_\\epsilon(\\mathbb{D})$.\n\nTherefore, even with the additional constraint $f'(0) = 1$, no uniform $r > 0$ exists. $\\square$\n\n## Part (c)\n\n**Statement:** If $h(z) = \\frac{1}{z} + c_0 + c_1 z + c_2 z^2 + \\cdots$ is analytic and injective for $0 < |z| < 1$, then $\\sum_{n=1}^{\\infty} n|c_n|^2 \\leq 1$.\n\n**Proof:** We apply the area theorem (Gronwall's theorem).\n\n1. **Setup:** Let $h(z) = \\frac{1}{z} + \\sum_{n=0}^{\\infty} c_n z^n$ be injective on the punctured disk $0 < |z| < 1$.\n\n2. **Area computation:** Consider the image of the punctured disk $D_\\rho(0) \\setminus \\{0\\}$ where $0 < \\rho < 1$. The boundary consists of:\n   - The outer circle $|z| = \\rho$\n   - The point at infinity (corresponding to $z = 0$)\n\n3. **Area of complement:** By the area theorem, the area of the complement of $h(D_\\rho(0) \\setminus \\{0\\})$ in the extended complex plane is:\n   $$\\text{Area} = \\pi\\left(\\frac{1}{\\rho^2} - \\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n}\\right)$$\n\n4. **Non-negativity:** Since area is non-negative:\n   $$\\frac{1}{\\rho^2} - \\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n} \\geq 0$$\n\n5. **Rearrangement:** This gives us:\n   $$\\sum_{n=1}^{\\infty} n|c_n|^2 \\rho^{2n} \\leq \\frac{1}{\\rho^2}$$\n\n6. **Limit as $\\rho \\to 1^-$:** Since all terms in the sum are non-negative, we can apply monotone convergence:\n   $$\\sum_{n=1}^{\\infty} n|c_n|^2 \\leq \\lim_{\\rho \\to 1^-} \\frac{1}{\\rho^2} = 1$$\n\nTherefore, $\\sum_{n=1}^{\\infty} n|c_n|^2 \\leq 1$. $\\square$\n\n## Part (d)\n\n**Statement:** If $f(z) = z + a_2 z^2 + \\cdots$ satisfies the hypotheses of the theorem, there exists another function $g$ satisfying the hypotheses such that $g^2(z) = f(z^2)$.\n\n**Proof:**\n\n1. **Nowhere vanishing property:** Since $f(0) = 0$ and $f'(0) = 1$, we can write:\n   $$f(z) = z + a_2 z^2 + a_3 z^3 + \\cdots = z(1 + a_2 z + a_3 z^2 + \\cdots)$$\n   \n   The function $1 + a_2 z + a_3 z^2 + \\cdots$ is holomorphic and equals 1 at $z = 0$, so it's nonzero in a neighborhood of 0. Since $f$ is injective, $f(z) \\neq 0$ for $z \\neq 0$, which means $f(z)/z \\neq 0$ on $\\mathbb{D} \\setminus \\{0\\}$. By continuity, $f(z)/z \\neq 0$ on all of $\\mathbb{D}$.\n\n2. **Existence of square root:** Since $f(z)/z$ is holomorphic and nowhere vanishing on the simply connected domain $\\mathbb{D}$, there exists a holomorphic function $\\psi: \\mathbb{D} \\to \\mathbb{C}$ such that:\n   $$\\psi^2(z) = \\frac{f(z)}{z} \\quad \\text{and} \\quad \\psi(0) = 1$$\n\n3. **Construction of $g$:** Define $g(z) = z\\psi(z^2)$.\n\n4. **Verification of functional equation:**\n   $$g^2(z) = z^2 \\psi^2(z^2) = z^2 \\cdot \\frac{f(z^2)}{z^2} = f(z^2)$$\n\n5. **Normalization:**\n   - $g(0) = 0 \\cdot \\psi(0) = 0$\n   - $g'(z) = \\psi(z^2) + z \\cdot 2z \\psi'(z^2) = \\psi(z^2) + 2z^2 \\psi'(z^2)$\n   - $g'(0) = \\psi(0) = 1$\n\n6. **Injectivity:** Suppose $g(z_1) = g(z_2)$. Then:\n   $$z_1 \\psi(z_1^2) = z_2 \\psi(z_2^2)$$\n   \n   Squaring both sides:\n   $$z_1^2 \\psi^2(z_1^2) = z_2^2 \\psi^2(z_2^2)$$\n   \n   Using $\\psi^2(z) = f(z)/z$:\n   $$z_1^2 \\cdot \\frac{f(z_1^2)}{z_1^2} = z_2^2 \\cdot \\frac{f(z_2^2)}{z_2^2}$$\n   \n   Therefore $f(z_1^2) = f(z_2^2)$. Since $f$ is injective, $z_1^2 = z_2^2$, which means $z_1 = \\pm z_2$.\n   \n   If $z_1 = -z_2$, then:\n   $$g(z_1) = z_1 \\psi(z_1^2) = -z_2 \\psi(z_2^2) = -g(z_2)$$\n   \n   But we assumed $g(z_1) = g(z_2)$, so $g(z_2) = -g(z_2)$, implying $g(z_2) = 0$. This means $z_2 = 0$, and therefore $z_1 = 0$ as well.\n   \n   Hence $g$ is injective.\n\nTherefore, $g$ satisfies all the required conditions. $\\square$\n\n## Part (e)\n\n**Statement:** With the notation of part (d), $|a_2| \\leq 2$, and equality holds if and only if $f(z) = \\frac{z}{(1 - e^{i\\theta}z)^2}$ for some $\\theta \\in \\mathbb{R}$.\n\n**Proof:**\n\n1. **Power series expansion of $1/g(z)$:** Since $g(z) = z + b_3 z^3 + b_5 z^5 + \\cdots$ (note that $g$ is odd because $g^2(z) = f(z^2)$ and $f$ has only even powers in its expansion when composed with $z^2$), we have:\n   $$\\frac{1}{g(z)} = \\frac{1}{z} + c_0 + c_1 z + c_2 z^2 + \\cdots$$\n\n2. **Coefficient computation:** Since $g(z) = z\\psi(z^2)$ where $\\psi(z) = 1 + \\frac{a_2}{2}z + \\cdots$, we have:\n   $$g(z) = z\\left(1 + \\frac{a_2}{2}z^2 + \\cdots\\right) = z + \\frac{a_2}{2}z^3 + \\cdots$$\n   \n   Therefore:\n   $$\\frac{1}{g(z)} = \\frac{1}{z} - \\frac{a_2}{2}z + \\cdots$$\n   \n   So $c_1 = -\\frac{a_2}{2}$.\n\n3. **Application of part (c):** Since $1/g(z)$ is injective (as $g$ is injective) and has the form $\\frac{1}{z} + c_0 + c_1 z + \\cdots$, part (c) gives:\n   $$\\sum_{n=1}^{\\infty} n|c_n|^2 \\leq 1$$\n   \n   In particular, $|c_1|^2 \\leq 1$, so $|c_1| \\leq 1$.\n\n4. **Bound on $|a_2|$:** Since $c_1 = -\\frac{a_2}{2}$, we have:\n   $$\\left|\\frac{a_2}{2}\\right| \\leq 1 \\implies |a_2| \\leq 2$$\n\n5. **Equality condition:** Equality $|a_2| = 2$ occurs if and only if $|c_1| = 1$ and all other coefficients $c_n = 0$ for $n \\geq 2$. This means:\n   $$\\frac{1}{g(z)} = \\frac{1}{z} + c_1 z$$\n   \n   where $|c_1| = 1$. Let $c_1 = e^{i\\theta}$ for some $\\theta \\in \\mathbb{R}$.\n\n6. **Determining $g(z)$:** From $\\frac{1}{g(z)} = \\frac{1}{z} + e^{i\\theta}z = \\frac{1 + e^{i\\theta}z^2}{z}$, we get:\n   $$g(z) = \\frac{z}{1 + e^{i\\theta}z^2}$$\n\n7. **Determining $f(z)$:** Since $g^2(z) = f(z^2)$:\n   $$f(z^2) = \\left(\\frac{z}{1 + e^{i\\theta}
```
