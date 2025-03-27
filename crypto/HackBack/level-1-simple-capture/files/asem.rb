require("openssl")
class Asem
  def self.e(msg, k, p: false)
    k, p_ = k.split(":").map(&:to_i)
    b = msg.bytes
    c = b.map { |x| x * k % p_ } 
    d = c.pack("Q*").force_encoding("UTF-8")
    d = d.unpack1("H*") if p
    d
  end

  def self.d(msg, k, p: false)
    k, p_ = k.split(":").map(&:to_i)
    f = p ? [msg].pack("H*").unpack("Q*") : msg.unpack("Q*")
    i = g(OpenSSL::BN.new(2).mod_exp(k, OpenSSL::BN.new(p_)).to_i, p_)
    r = f.map { |x| x * i % p_ }
    r.pack("C*")
  end

  def self.g(a, m)
    m0, x0, x1 = m, 0, 1
    return 0 if m == 1
    while a > 1
      q = a / m
      m, a = a % m, m
      x0, x1 = x1 - q * x0, x0
    end
    x1 += m0 if x1.negative?
    x1
  end
end