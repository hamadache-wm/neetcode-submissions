class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false

        const sMap = this.countCharOfString(s);
        const tMap = this.countCharOfString(t);

        for (const v of Object.keys(sMap)) {
            if (sMap[v] !== tMap[v]) return false
        }

        return true
    }

    countCharOfString(str) {
        const map = new Map();

        for (const v of str) {
            map[v] = map[v] ? map[v]+=1 : 1
        }

        return map
    }
}
