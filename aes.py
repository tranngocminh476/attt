# ==========================================
# CÁC BẢNG HẰNG SỐ CỦA AES (CHUẨN RIJNDAEL)
# ==========================================
SBOX = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

INV_SBOX = [SBOX.index(x) for x in range(256)] # Tạo bảng InvSbox từ Sbox
RCON = [0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]

# ==========================================
# CÁC HÀM TOÁN HỌC TRƯỜNG GALOIS GF(2^8)
# ==========================================
def gmul(a, b):
    """Nhân 2 số trong trường Galois GF(2^8)."""
    p = 0
    for _ in range(8):
        if b & 1: p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set: a ^= 0x1b
        b >>= 1
    return p % 256

# ==========================================
# LỚP MÃ HÓA AES-128
# ==========================================
class AES128:
    def __init__(self, key: bytes):
        if len(key) != 16: raise ValueError("Khóa phải dài 16 bytes (128-bit)")
        self.round_keys = self._expand_key(list(key))

    def _sub_word(self, word):
        return [SBOX[b] for b in word]

    def _rot_word(self, word):
        return word[1:] + word[:1]

    def _expand_key(self, key):
        """Mở rộng khóa 16 bytes thành 176 bytes (11 khóa con x 16 bytes)"""
        keys = key[:]
        for i in range(4, 44):
            word = keys[(i-1)*4 : i*4]
            if i % 4 == 0:
                word = self._sub_word(self._rot_word(word))
                word[0] ^= RCON[i // 4]
            prev_word = keys[(i-4)*4 : (i-3)*4]
            keys.extend([prev_word[j] ^ word[j] for j in range(4)])
        return keys

    # --- CÁC PHÉP TOÁN TRONG 1 VÒNG LẶP ---
    def _add_round_key(self, state, round_key):
        return [s ^ k for s, k in zip(state, round_key)]

    def _sub_bytes(self, state):
        return [SBOX[b] for b in state]
    
    def _inv_sub_bytes(self, state):
        return [INV_SBOX[b] for b in state]

    def _shift_rows(self, state):
        # State lưu dưới dạng mảng 1 chiều cột-chính (column-major)
        s = state
        return [
            s[0], s[5], s[10], s[15],
            s[4], s[9], s[14], s[3],
            s[8], s[13], s[2], s[7],
            s[12], s[1], s[6], s[11]
        ]

    def _inv_shift_rows(self, state):
        s = state
        return [
            s[0], s[13], s[10], s[7],
            s[4], s[1], s[14], s[11],
            s[8], s[5], s[2], s[15],
            s[12], s[9], s[6], s[3]
        ]

    def _mix_columns(self, state):
        s = [0]*16
        for c in range(4): # Xử lý từng cột
            col = state[c*4 : (c+1)*4]
            s[c*4+0] = gmul(0x02, col[0]) ^ gmul(0x03, col[1]) ^ col[2] ^ col[3]
            s[c*4+1] = col[0] ^ gmul(0x02, col[1]) ^ gmul(0x03, col[2]) ^ col[3]
            s[c*4+2] = col[0] ^ col[1] ^ gmul(0x02, col[2]) ^ gmul(0x03, col[3])
            s[c*4+3] = gmul(0x03, col[0]) ^ col[1] ^ col[2] ^ gmul(0x02, col[3])
        return s

    def _inv_mix_columns(self, state):
        s = [0]*16
        for c in range(4):
            col = state[c*4 : (c+1)*4]
            s[c*4+0] = gmul(0x0e, col[0]) ^ gmul(0x0b, col[1]) ^ gmul(0x0d, col[2]) ^ gmul(0x09, col[3])
            s[c*4+1] = gmul(0x09, col[0]) ^ gmul(0x0e, col[1]) ^ gmul(0x0b, col[2]) ^ gmul(0x0d, col[3])
            s[c*4+2] = gmul(0x0d, col[0]) ^ gmul(0x09, col[1]) ^ gmul(0x0e, col[2]) ^ gmul(0x0b, col[3])
            s[c*4+3] = gmul(0x0b, col[0]) ^ gmul(0x0d, col[1]) ^ gmul(0x09, col[2]) ^ gmul(0x0e, col[3])
        return s

    # --- MÃ HÓA/GIẢI MÁ 1 KHỐI (16 BYTES) ---
    def encrypt_block(self, block: list) -> list:
        state = self._add_round_key(block, self.round_keys[0:16])
        for i in range(1, 10):
            state = self._sub_bytes(state)
            state = self._shift_rows(state)
            state = self._mix_columns(state)
            state = self._add_round_key(state, self.round_keys[i*16 : (i+1)*16])
        
        # Vòng cuối không có MixColumns
        state = self._sub_bytes(state)
        state = self._shift_rows(state)
        state = self._add_round_key(state, self.round_keys[160:176])
        return state

    def decrypt_block(self, block: list) -> list:
        state = self._add_round_key(block, self.round_keys[160:176])
        for i in range(9, 0, -1):
            state = self._inv_shift_rows(state)
            state = self._inv_sub_bytes(state)
            state = self._add_round_key(state, self.round_keys[i*16 : (i+1)*16])
            state = self._inv_mix_columns(state)
            
        state = self._inv_shift_rows(state)
        state = self._inv_sub_bytes(state)
        state = self._add_round_key(state, self.round_keys[0:16])
        return state

# ==========================================
# CÁC HÀM TIỆN ÍCH (PADDING & SỬ DỤNG)
# ==========================================
def pad(data: bytes) -> bytes:
    """Kỹ thuật PKCS#7 Padding"""
    padding_len = 16 - (len(data) % 16)
    return data + bytes([padding_len] * padding_len)

def unpad(data: bytes) -> bytes:
    padding_len = data[-1]
    return data[:-padding_len]

# Chạy thử nghiệm thuật toán từ đầu
if __name__ == "__main__":
    # Khóa 16 bytes (128-bit)
    key = b"MySuperSecretKey" 
    aes = AES128(key)
    
    # Dữ liệu cần mã hóa
    text = "Hello, thuật toán AES được viết hoàn toàn bằng Python thuần!"
    print(f"Bản rõ gốc: {text}")
    
    # 1. Độn dữ liệu (Padding)
    padded_data = pad(text.encode('utf-8'))
    
    # 2. Mã hóa từng khối 16 bytes (Chế độ ECB đơn giản)
    encrypted_bytes = []
    for i in range(0, len(padded_data), 16):
        block = list(padded_data[i:i+16])
        encrypted_block = aes.encrypt_block(block)
        encrypted_bytes.extend(encrypted_block)
        
    print(f"Bản mã (Hex): {bytes(encrypted_bytes).hex()}")
    
    # 3. Giải mã từng khối
    decrypted_bytes = []
    for i in range(0, len(encrypted_bytes), 16):
        block = encrypted_bytes[i:i+16]
        decrypted_block = aes.decrypt_block(block)
        decrypted_bytes.extend(decrypted_block)
        
    # 4. Gỡ bỏ padding
    final_text = unpad(bytes(decrypted_bytes)).decode('utf-8')
    print(f"Sau giải mã: {final_text}")