# ==========================================
# CÁC BẢNG HẰNG SỐ CHUẨN CỦA DES (1-indexed)
# ==========================================

# Hoán vị ban đầu (Initial Permutation - IP)
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]
# Hoán vị kết thúc (Final Permutation - FP / IP^-1)
FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# Bảng mở rộng (Expansion - E) từ 32 bit lên 48 bit
E_BOX = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# Bảng hoán vị P (P-box) trong hàm Feistel
P_BOX = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

# PC-1: Nén khóa 64 bit thành 56 bit (loại bỏ parity bits)
PC1 = [
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
]

# PC-2: Chọn 48 bit từ 56 bit để tạo khóa con
PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# Lịch dịch trái vòng theo từng vòng lặp (16 vòng)
SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# 8 Hộp S-box (Mỗi hộp 4x16)
S_BOXES = [
    # S1
    [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
     [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
     [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
     [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],
    # S2
    [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
     [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
     [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
     [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],
    # S3
    [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
     [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
     [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
     [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],
    # S4
    [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
     [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
     [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
     [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],
    # S5
    [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
     [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
     [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
     [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],
    # S6
    [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
     [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
     [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
     [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],
    # S7
    [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
     [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
     [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
     [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],
    # S8
    [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
     [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
     [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
     [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
]

# ==========================================
# CÁC HÀM TIỆN ÍCH XỬ LÝ BIT VÀ CHUỖI
# ==========================================
def permute(block, table):
    """Hoán vị các bit trong block theo chỉ mục của bảng table."""
    return [block[i - 1] for i in table]

def xor(bits1, bits2):
    """Thực hiện phép XOR giữa 2 mảng bit."""
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def left_shift(bits, n):
    """Dịch trái xoay vòng mảng bit."""
    return bits[n:] + bits[:n]

def bytes_to_bits(data):
    """Chuyển đổi chuỗi bytes thành mảng bit."""
    bits = []
    for byte in data:
        bits.extend([int(b) for b in format(byte, '08b')])
    return bits

def bits_to_bytes(bits):
    """Chuyển đổi mảng bit trở lại chuỗi bytes."""
    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte_val = int(''.join(map(str, bits[i:i+8])), 2)
        byte_array.append(byte_val)
    return bytes(byte_array)

def pad(data):
    """PKCS#7 Padding: Thêm các byte cho đủ bội số của 8 (64 bit)."""
    pad_len = 8 - (len(data) % 8)
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    """Loại bỏ PKCS#7 Padding."""
    pad_len = data[-1]
    return data[:-pad_len]

# ==========================================
# LỚP MÃ HÓA DES
# ==========================================
class DES_Scratch:
    def __init__(self, key: bytes):
        if len(key) != 8:
            raise ValueError("Khóa DES bắt buộc phải dài 8 bytes (64 bit).")
        key_bits = bytes_to_bits(key)
        self.round_keys = self._generate_keys(key_bits)

    def _generate_keys(self, key_bits):
        """Sinh ra 16 khóa con (mỗi khóa 48 bit) từ khóa chính."""
        keys = []
        # PC-1: 64 bit -> 56 bit
        key_56 = permute(key_bits, PC1)
        # Tách làm 2 nửa
        L, R = key_56[:28], key_56[28:]
        
        for shift in SHIFTS:
            L = left_shift(L, shift)
            R = left_shift(R, shift)
            # Gộp lại và đưa qua PC-2: 56 bit -> 48 bit
            round_key = permute(L + R, PC2)
            keys.append(round_key)
        return keys

    def _f_function(self, right_half, round_key):
        """Hàm Feistel (E-box -> XOR -> S-box -> P-box)."""
        # Mở rộng 32 bit lên 48 bit
        expanded = permute(right_half, E_BOX)
        # XOR với khóa vòng
        xored = xor(expanded, round_key)
        
        # Đưa qua 8 S-box
        s_box_out = []
        for i in range(8):
            # Tách thành từng nhóm 6 bit
            chunk = xored[i * 6 : (i + 1) * 6]
            # Bit đầu và cuối tạo thành hàng (0-3)
            row = (chunk[0] << 1) | chunk[5]
            # 4 bit giữa tạo thành cột (0-15)
            col = (chunk[1] << 3) | (chunk[2] << 2) | (chunk[3] << 1) | chunk[4]
            
            # Tra S-box
            val = S_BOXES[i][row][col]
            # Chuyển giá trị (0-15) thành mảng 4 bit
            s_box_out.extend([int(b) for b in format(val, '04b')])
            
        # Cuối cùng đưa qua P-box hoán vị 32 bit
        return permute(s_box_out, P_BOX)

    def _process_block(self, block_bits, decrypt=False):
        """Xử lý mã hóa hoặc giải mã một khối 64 bit (Mạng Feistel)."""
        # Hoán vị IP
        block = permute(block_bits, IP)
        L, R = block[:32], block[32:]
        
        # Giải mã thì đảo ngược thứ tự khóa (Vòng 16 -> 1)
        keys = self.round_keys[::-1] if decrypt else self.round_keys
        
        # 16 Vòng Feistel
        for key in keys:
            next_L = R
            next_R = xor(L, self._f_function(R, key))
            L, R = next_L, next_R
            
        # Đảo 2 nửa ở vòng cuối (R + L) và Hoán vị kết thúc FP
        return permute(R + L, FP)

    def encrypt(self, plaintext: str) -> bytes:
        """Mã hóa văn bản (áp dụng Padding và chế độ ECB)."""
        padded = pad(plaintext.encode('utf-8'))
        encrypted_bits = []
        
        # Chạy từng khối 8 bytes (64 bit)
        for i in range(0, len(padded), 8):
            block_bits = bytes_to_bits(padded[i:i+8])
            cipher_bits = self._process_block(block_bits, decrypt=False)
            encrypted_bits.extend(cipher_bits)
            
        return bits_to_bytes(encrypted_bits)

    def decrypt(self, ciphertext: bytes) -> str:
        """Giải mã văn bản và gỡ padding."""
        decrypted_bits = []
        
        for i in range(0, len(ciphertext), 8):
            block_bits = bytes_to_bits(ciphertext[i:i+8])
            plain_bits = self._process_block(block_bits, decrypt=True)
            decrypted_bits.extend(plain_bits)
            
        padded_text = bits_to_bytes(decrypted_bits)
        return unpad(padded_text).decode('utf-8')

# ==========================================
# CHẠY THỬ NGHIỆM
# ==========================================
if __name__ == "__main__":
    # Khóa DES bắt buộc là 8 bytes
    key = b"MySecKey" 
    des = DES_Scratch(key)
    
    text = "Mã hóa DES cài đặt hoàn toàn bằng Python thuần từ con số 0!"
    print(f"Bản rõ gốc: {text}")
    print(f"Khóa: {key}\n")
    
    # Mã hóa
    encrypted_bytes = des.encrypt(text)
    print(f"Bản mã (Hex): {encrypted_bytes.hex().upper()}\n")
    
    # Giải mã
    decrypted_text = des.decrypt(encrypted_bytes)
    print(f"Bản giải mã: {decrypted_text}")
