# iOS uitableview 判断滚动尽头

```swift
func didScrollViewDidScroll(_ scrollView: UIScrollView) {
        guard !contentView.subviews.isEmpty && contentView.bounds.width > 0 else { return }
        
        let scrollViewWidth = scrollView.bounds.width
        if let first = contentView.subviews.last (where: { $0.frame.origin.x + $0.frame.width - scrollView.contentOffset.x <= scrollViewWidth }),
           let index = contentView.subviews.firstIndex(of: first) {
            if !revealedItemIndices.contains(index) {
                let newlyRevealedIndices = Set(0...index).subtracting(revealedItemIndices)
                if !newlyRevealedIndices.isEmpty {
                    revealedItemIndices = revealedItemIndices.union(newlyRevealedIndices)
                    delegate?.didHotTopicItemReveal(in: self, with: Array(newlyRevealedIndices).sorted())
                }
            }
        }
        
        if AppManager.isWeekendWeekly || AppManager.isNewMonday {
            let sfw = scrollView.frame.size.width
            let xoff = scrollView.contentOffset.x
            let toright = scrollView.contentSize.width - xoff
            print("distanceFromRight sfw=\(sfw) xoff=\(xoff) toright=\(toright)")
            if toright <= sfw {
                print("distanceFromRight=last")
                ivRightMore.isHidden = true
            } else {
                ivRightMore.isHidden = false
            }
            
            if xoff > 0 {
                ivLeftMore.isHidden = true
            } else {
                ivLeftMore.isHidden = false
            }
        }
    }
```