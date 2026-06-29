import "reflect"
func isAnagram(s string, t string) bool {
    arrayS := []rune(s)
    arrayT := []rune(t)

    mapS := make(map[rune]int)
    mapT := make(map[rune]int)
    
    if len(s) != len(t) {
        return false
    } else {
        for i := 0; i < len(arrayS); i++ {
            charS := arrayS[i]
            charT := arrayT[i]
            _, ok := mapS[charS]
             
             if ok {
                mapS[charS] = mapS[charS] + 1
             } else {
                mapS[charS] = 1
             }

             _, ok = mapT[charT]

             if ok {
                mapT[charT] = mapT[charT] + 1
             } else {
                mapT[charT] = 1
             }
        }

        return reflect.DeepEqual(mapS, mapT)
    }
}
