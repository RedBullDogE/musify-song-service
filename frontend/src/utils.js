export function isEqual(obj1, obj2) {
    let objectsAreSame = true

    if (obj1.length !== obj2.length) {
        return false
    }

    for (let propertyName in obj1) {
        if (obj1[propertyName] !== obj2[propertyName]) {
            objectsAreSame = false;
            break;
        }
    }
    return objectsAreSame;
}

