from utils.eval_utils import evaluate_standard

if __name__ == "__main__":
    # dummy labels
    gt_labels = ["SUPPORTS", "REFUTES", "REFUTES", "SUPPORTS", "REFUTES"]
    pred_labels = ["REFUTES", "REFUTES", "SUPPORTS", "SUPPORTS", "SUPPORTS"]

    accuracy, f1score = evaluate_standard(gt_labels, pred_labels)

    if accuracy == 0.4 and f1score == 0.4:
        print("Your `evaluate_standard` function is CORRECT!")

    else:
        raise NotImplementedError(
            "Your `evaluate_standard` function is INCORRECT!")