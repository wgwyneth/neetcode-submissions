type Solution struct{}

func (s *Solution) Encode(strs []string) string {
    delim := '世'
    encoded := ""

    for _, str := range strs {
        encoded += str + string(delim)
    }

    return encoded
}

func (s *Solution) Decode(encoded string) []string {
    delim := '世'
    decoded := []string{}
    str := ""
    for _, char := range []rune(encoded) {
        if char == delim {
            decoded = append(decoded, str)
            str = ""
        } else {
            str += string(char)
        }
    }

    return decoded
}
